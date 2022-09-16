#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    
    ofBackground(0);
    ofDisableArbTex();
    
    camera.setPosition(vec3(0.0f, 8.0f, 24.0f));
    camera.setTarget(vec3(0.0f, 4.0f, 0.0f));
    camera.setFov(32.0f);
    camera.setNearClip(0.05f);
    camera.setFarClip(100.0f);
    camera.setAutoDistance(false);
    
    ofxAssimpModelLoader tempModel;
    tempModel.loadModel("m281.obj");
    bunny = tempModel.getMesh(0);
    
    
    surfaceShader.load("simplePhong");
    matAmbient = vec4(0.1f, 0.1f, 0.2f, 1.0f);
    matDiffuse = vec4(0.2f, 0.5f, 0.7f, 1.0f);
    matSpecular =  vec4(3.5f, 4.0f, 5.0f, 1.0f);
    matShininess = 500.0f;
    lightPosition = vec4(10.0f, 10.0f, 20.0f, 1.0f);
    lightColor = vec4(1.0f, 1.0f, 0.8f, 1.0f);
    
    matReflectivity = 0.3;
   // environmentMap.load("hdri_hub_environmentMap.jpg");
    
    
    matTransparency = 0.7;
    matRefractiveIndex = 1.5;

}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){

    ofEnableDepthTest();
    camera.begin();
    surfaceShader.begin();
    surfaceShader.setUniform4f("matAmbient", matAmbient);
    surfaceShader.setUniform4f("matDiffuse", matDiffuse);
    surfaceShader.setUniform4f("matSpecular", matSpecular);
    surfaceShader.setUniform1f("matShininess", matShininess);
    surfaceShader.setUniform4f("lightPosition", lightPosition);
    surfaceShader.setUniform4f("lightColor", lightColor);
    surfaceShader.setUniform1f("matReflectivity", matReflectivity);
    surfaceShader.setUniformTexture("environmentMap", environmentMap.getTexture(), 1);
    surfaceShader.setUniform1f("matRefractivity", matTransparency);
    surfaceShader.setUniform1f("matRefractiveIndex", matRefractiveIndex);
    bunny.draw();
    surfaceShader.end();
    ofDrawGrid(2.0f, 10, false, false, true, false);
    camera.end();
}


//--------------------------------------------------------------
void ofApp::keyPressed(int key){

}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
