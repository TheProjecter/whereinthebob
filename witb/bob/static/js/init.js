        window.onload = function () {
            var R = Raphael("paper", 462, 540);
            var attr = {
                fill: "#fff",
                stroke: "#000",
                "stroke-width": 1,
                "stroke-linejoin": "round"
            };

 			var current = null;
            for (var room in plan) {

                plan[room] = R.path(plan[room]).attr(attr);

                plan[room].scale(0.6,0.6,0,0);
                // plan[room].color = Raphael.getColor();
                plan[room].color = "green";
                (function (st, room) {
                    st[0].style.cursor = "pointer";
                    if(dont.indexOf(room) == -1 ){
	                    st[0].onmouseover = function () {
	                        // current && plan[current].animate({fill: "#333", stroke: "#666"}, 500);
	                        st.animate({fill: st.color, stroke: "#ccc"}, 500);
	                        st.toFront();
	                        R.safari();
	                        current = room;
	                    };
	                    st[0].onmouseout = function () {
	                        st.animate({fill: "#fff", stroke: "#666"}, 500);
	                        st.toFront();
	                        R.safari();
	                    };
	                }
                })(plan[room], room);
            }
        };