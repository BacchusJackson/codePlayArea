import { Component, OnInit } from '@angular/core';
import {ValidateService} from '../../services/validate.service';
import {FlashMessagesService} from 'angular2-flash-messages';
import {AuthService} from '../../services/auth.service';
import {Router} from '@angular/router'

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  name: String;
  username: String;
  email: String;
  password: String;

  constructor(
    private validateService: ValidateService, 
    private flashMessage: FlashMessagesService,
    private authService: AuthService,
    private router: Router
    ) { }

  ngOnInit() {
  }
  
  onRegisterSubmit() {
    const user = {
      name: this.name,
      email: this.email,
      username: this.username,
      password: this.password
    }
  
  //required Fields
    if(!this.validateService.validateRegister(user)) {
      this.flashMessage.show('Please fill in all fields', {cssClass: 'alert-danger', time: 3000});
      return false;
    }
    //Checks for the correct email
    if(!this.validateService.validateEmail(user.email)) {
      this.flashMessage.show('Please use a proper email', {cssClass: 'alert-danger', time: 3000});
      return false;
    }
    
    //Register User
    this.authService.registerUser(user).subscribe(data => {
      if(data.success) {
        
        this.flashMessage.show('You are now registered!', {cssClass: 'alert-success', time: 3000});
        this.router.navigate(['/']);
      } else {
          this.flashMessage.show('uh oh! Something went wrong...', {cssClass: 'alert-danger', time: 3000});
          this.router.navigate(['/register']);
        
      }
    })
  }

}