function initGUI(){
  var is_clipping=true;
  var gui = new dat.GUI(),


  folderChromosome= gui.addFolder( 'Chromosome' ),
  propsChromosome = {

    get 'Visible'() {
      return thick_line.visible;
    },

    set 'Visible'( v ) {
      thick_line.visible = v;
    },

    get 'Line Width'() {
      return matLine.linewidth;
    },

    set 'Line Width'( v ) {
      matLine.linewidth = v;
    }

  };


    folderGlobal = gui.addFolder( 'Clipping' ),
    propsGlobal = {

      get 'Enabled'() {
        return !is_clipping;
      },

      set 'Enabled'( v ) {
        is_clipping = false;
        matLine.clippingPlanes = [globalPlane] ;
        materialSphere.clippingPlanes = [globalPlane] ;
        console.log(thick_line)
      },

      get 'Plane'() {
        return globalPlane.constant;
      },

      set 'Plane'( v ) {
        globalPlane.constant = v;
      }

    };

    folderplane = gui.addFolder( 'Helper Plane' ),
    propsplane = {

      get 'Enabled'() {
        return helpers.visible;
      },

      set 'Enabled'( v ) {
        console.log(v);
        helpers.visible = v;
      },
    };

    foldergene = gui.addFolder( 'Genes' ),
    propsgene = {

      get 'Enabled'() {
        return geneGroup.visible;
      },

      set 'Enabled'( v ) {
        console.log(v);
        geneGroup.visible = v;
      },
    };


  folderChromosome.add( propsChromosome, 'Visible' );
  folderChromosome.add( propsChromosome, 'Line Width', 0.0, 25.0 );
  folderGlobal.add( propsGlobal, 'Enabled' );
  folderGlobal.add( propsGlobal, 'Plane', - r/2, r/2 );
  folderplane.add( propsplane, 'Enabled' );
  foldergene.add( propsgene, 'Enabled' );

  // Start

  startTime = Date.now();
}
