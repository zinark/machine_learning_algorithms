def d1():
    pc = 0.01
    pnc = 0.99
    p_pos_given_c = 0.9
    p_neg_given_c = 0.1
    p_neg_given_nc = 0.9
    p_pos_given_nc = 0.1
    # P(C , neg) = P(C)  * P(neg | C)
    # P(C', neg) = P(C') * P(neg | C')
    p_joint_c_neg = pc * p_neg_given_c
    p_joint_nc_neg = pnc * p_neg_given_nc
    print "P(C , neg)", p_joint_c_neg
    print "P(C', neg)", p_joint_nc_neg
    # P(neg) = P(C , neg) + P(C', neg)
    p_neg_norm = p_joint_c_neg + p_joint_nc_neg
    print "P(C , neg) / P(neg)", p_joint_c_neg / p_neg_norm
    print "P(C', neg) / P(neg)", p_joint_nc_neg / p_neg_norm

def b_dist():
    # P(C)                                              # P('C)
    p_c             = 0.1                               ;p_nc           = 0.9
    # P(Pos|C)                                          # P(Neg|C)
    p_pos_given_c   = 0.9                               ;p_neg_given_c  = 0.1
    # P(Neg|C')                                         # P(Pos|C')
    p_neg_given_nc  = 0.5                               ;p_pos_given_nc = 0.5

    # P(C , neg) = P(C)  * P(neg | C)
    p_joint_c_neg = p_c * p_neg_given_c

    # P(C', neg) = P(C') * P(neg | C')
    p_joint_nc_neg = p_nc * p_neg_given_nc

    print "P(C , neg)", p_joint_c_neg
    print "P(C', neg)", p_joint_nc_neg

    # P(neg) = P(C , neg) + P(C', neg)
    p_neg_norm = p_joint_c_neg + p_joint_nc_neg
    print "P(neg)", p_neg_norm

    print "P(C |neg) = P(C , neg) / P(neg)", round (p_joint_c_neg / p_neg_norm,3)
    print "p(C'|Neg) = P(C', neg) / P(neg)", round (p_joint_nc_neg / p_neg_norm,3)

    # _poss
    print;print;

    # P(C , pos) = P(C)  * P(pos | C)
    p_joint_c_pos = p_c * p_pos_given_c

    # P(C', pos) = P(C') * P(pos | C')
    p_joint_nc_pos = p_nc * p_pos_given_nc

    print "P(C , pos)", p_joint_c_pos
    print "P(C', pos)", p_joint_nc_pos

    # P(pos) = P(C , pos) + P(C', pos)
    p_pos_norm = p_joint_c_pos + p_joint_nc_pos
    print "P(pos)", p_pos_norm

    print "P(C |pos) = P(C , pos) / P(pos)", round (p_joint_c_pos / p_pos_norm,3)
    print "p(C'|pos) = P(C', pos) / P(neg)", round (p_joint_nc_pos / p_pos_norm,3)


b_dist()