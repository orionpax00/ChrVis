function onDocumentMouseDown(event) {

    var isdone = false

if (!isdone){
    // requestAnimationFrame( onDocumentMouseDown );

    event.preventDefault();


    isdone = true;

    mouseYOnMouseDown = - ( event.clientY / window.innerHeight ) * 2 + 1
    mouseXOnMouseDown = ( event.clientX / window.innerWidth ) * 2 - 1;

    var vector = new THREE.Vector3((event.clientX / window.innerWidth) * 2 - 1, -(event.clientY / window.innerHeight) * 2 + 1, 0.5);
    vector = vector.unproject(camera);

    var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());
    var intersects = raycaster.intersectObjects(scene.children, true); // Circle element which you want to identify

    if (intersects[0]){

      x_ = intersects[0].object.position.x
      y_ = intersects[0].object.position.y
      z_ = intersects[0].object.position.z

      // console.log(intersects[0])
      var lineObject = scene.getObjectByName( "line" );
      var geneClickedObject = scene.getObjectByName( "clicked_gene" );
      var helperObject = scene.getObjectByName( "dir_helper" );

      scene.remove(geneClickedObject)
      scene.remove(helperObject)

      // geneGroup.visible = false;


      var geometryClickedSphere = new THREE.SphereGeometry( 0.2, 50,50 );
      var materialClickedSphere = new THREE.MeshBasicMaterial( {color: 0xf99999} );

      var sphere = new THREE.Mesh( geometryClickedSphere, materialClickedSphere );
      sphere.position.set(intersects[0].object.position.x, intersects[0].object.position.y, intersects[0].object.position.z);
      sphere.name = "clicked_gene"
      sphere.userData.name = intersects[0].object.userData.name;
      scene.add( sphere );


      var dir = new THREE.Vector3( x_, y_, z_ );

      //normalize the direction vector (convert to vector of length 1)
      dir.normalize();

      // camera.position.x = x_;
      // camera.position.y = y_;
      // camera.position.z = z_;
      //
      // camera.lookAt( scene.position );
      //
      // camera.position.x *= 1.3;
      // camera.position.y *= 1.3;
      // camera.position.z *= 1.3;

      var origin = new THREE.Vector3( 0, 0, 0 );
      var length = Math.sqrt(x_ * x_ + y_ * y_ + z_ * z_);
      var hex = 0xffffff;

      var arrowHelper = new THREE.ArrowHelper( dir, origin, length, hex , headLength = 0.02 * length);
      arrowHelper.name = "dir_helper"
      scene.add( arrowHelper );



      // console.log(thick_line);
      thick_line.material.linewidth = 1;
      // thick_line.material.wireframe = true;
      // thick_line.material.wireframeLinewidth = 0.2;
      thick_line.material.color.setHex( 0xffffff );
      // thick_line.material.lights = true;

      var ringObject = scene.getObjectByName( "ring" );
      scene.remove(ringObject)



      var geometry = new THREE.RingGeometry( 0.5, 0.55, 32 );
      var material = new THREE.MeshBasicMaterial( { color: 0xffffff, side: THREE.DoubleSide } );
      var mesh = new THREE.Mesh( geometry, material );
      mesh.name = "ring"
      mesh.position.set(intersects[0].object.position.x, intersects[0].object.position.y, intersects[0].object.position.z)
      // console.log(intersects[0].object.position.x)
      scene.add(mesh)

      var tootlip = document.getElementById('tooltip');
      tooltip.innerHTML = "<span> Gene Name: "+ intersects[0].object.userData.name + "<br /> Length form origin: " + length.toFixed(3) + "<br /> Present on Chromosome: " + Math.floor(Math.random() * Math.floor(23)) + "</span>";
      nav_geneclicked()
    }


}
}
