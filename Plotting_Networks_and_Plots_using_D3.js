<!DOCTYPE html>
<html>
<head>
<meta charset = 'utf-8'>

<script src = 'https://d3js.org/d3.v4.js'></script>
</head>
<div id="my_dataviz"></div>
<script>
var margin = {top: 10, right: 30, bottom: 30, left: 40},
width = 400 - margin.left - margin.right,
height = 400 - margin.top - margin.bottom;

var svg = d3.select('#my_dataviz')
.append('svg')
.attr('width', width + margin.left + margin.right)
.attr('height', height + margin.top + margin.bottom)
.append('g')
.attr('transform',
'translate(' + margin.left + ',' + margin.top + ')');

d3.json('https://raw.githubusercontent.com/holtzy/D3-graph-
gallery/master/DATA/data_network.json', function(data){

var link = svg
.selectAll('line')
.data(data.links)
.enter()
.append('line')
.style('stroke', '#aaa')

var node=svg
.selectAll('circle')
.data(data.nodes)
.enter()
.append('circle')
.attr('r', 20)
.style('fill', '#69b3a2')

var simulation = d3.forceSimulation(data.nodes)
.force('link', d3.forceLink()
.id(function(d) {return d.id;})
.links(data.links)
)
.force('charge', d3.forceManyBody().strength(-400))
.force('center', d3.forceCenter(width/2, height/2))
.on('end', ticked);

function ticked(){
  link
.attr('x1', function(d) {return d.source.x;})
.attr('y1', function(d) {return d.source.y;})
.attr('x2', function(d) {return d.target.x;})
.attr('y2', function(d) {return d.target.y;});
node.attr('cx', function(d) {return d.x+6;})
.attr('cy', function(d) {return d.y-6});
}
});
</script>
</html>
