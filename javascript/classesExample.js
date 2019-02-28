class Mission {
    constructor(ato) {
        this.ato = ato.toUpperCase();
        this.targets = [];
    }
};

class Target {
    constructor(name, beNumber) {
        this.name = name.toUpperCase();
        this.beNumber = beNumber.toUpperCase();
        this.callOuts = [];
        this.scenes = [];
    }
} ;

class Scene {
    constructor(number, migDetects, planeDetects) {
        this.number = number;
        this.migDetects = migDetects;
        this.planeDetects = planeDetects;
    }
}

class AnalystCallout {
    constructor(ob, count) {
        this.ob;
        this.count;
    }
}

const missions = [];

missions[0] = new Mission('msn103');
missions[1] = new Mission('msn104');

missions[0].targets[0] = new Target('chicago', '32093');

missions[0].targets[0].scenes[0] = new Scene(10, 402, 3);

console.log(missions[0].targets[0].scenes[0].number);

console.log(JSON.stringify(missions));
