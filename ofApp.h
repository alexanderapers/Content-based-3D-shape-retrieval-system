#pragma once

#include "ofxAssimpModelLoader.h"
#include "ofMain.h"

using namespace glm;

class ofApp : public ofBaseApp{

	public:
		void setup();
		void update();
		void draw();
       

		void keyPressed(int key);
		void keyReleased(int key);
		void mouseMoved(int x, int y );
		void mouseDragged(int x, int y, int button);
		void mousePressed(int x, int y, int button);
		void mouseReleased(int x, int y, int button);
		void mouseEntered(int x, int y);
		void mouseExited(int x, int y);
		void windowResized(int w, int h);
		void dragEvent(ofDragInfo dragInfo);
		void gotMessage(ofMessage msg);
    
    ofEasyCam camera;
    ofVboMesh bunny;
    
   // ofShader surfaceShader;
    vec4 matAmbient;
    vec4 matDiffuse;
    vec4 matSpecular;
    float matShininess;
    vec4 lightPosition;
    vec4 lightColor;
    
    ofImage environmentMap;
    float matReflectivity;
    
    float matTransparency;
    float matRefractiveIndex;
    
		
};
