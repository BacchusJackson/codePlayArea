const callouts = [{obName:'',obCount:''}];
const scenes = [{number:null,migDetects:null,planeDetects:null}];
const targets = [{name:'', beNumber:'', callouts:callouts, scenes:scenes}];
const missions = [{ato:'', targets:targets}];


missions[0].ato = 'msn001';
missions[0].targets[0].name = 'chicago';
missions[0].targets[0].beNumber = '40293';
missions[0].targets[0].callouts[0].obName = 'Labador Retriever';
missions[0].targets[0].callouts[0].obCount = 24;
missions[0].targets[0].scenes[0].number = 9083;
missions[0].targets[0].scenes[0].migDetects = 3021;
missions[0].targets[0].scenes[0].planeDetects = 21;


console.log(missions[0].targets[0].name);

jString = JSON.stringify(missions);

console.log(jString);
