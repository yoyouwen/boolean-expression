from simbool.proposition import Prop
from simbool.simplify import simplify

cont33=Prop("cont33")
cont28=Prop("cont28")
cond=Prop("cond")
cont43=Prop("cont43")
cont36=Prop("cont36")
cont54=Prop("cont54")
cont47=Prop("cont47")


A, B, C = [Prop(x) for x in "ABC"]
p=( cont33 & cont28 & cond)|  (cont43 & cont36 & ~ cont28 & cond)| (cont43 & cont36 & ~cont33 & cont28 & cond)  |(cont54 & cont47 & ~ cont36 & ~ cont28 & cond) |(cont54& cont47 & ~cont36 & ~cont33 & cont28 &  cond) |(cont54 & cont47 & ~ cont43 & cont36 & ~ cont33 & cont28 & cond)

#Boolean expr=T: invoke.cont54=T && invoke.cont47=T && invoke.cont43=F && invoke.cont36=T && invoke.cont33=F && invoke.cont28=T &&  for.cond=T   


p1=(simplify(p))
print('result',p1)