# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterPublicIpReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'eip': 'CreateClusterPublicEip',
        'elb_white_list_req': 'CreateClusterElbWhiteList',
        'public_bind_type': 'str',
        'eip_id': 'str'
    }

    attribute_map = {
        'eip': 'eip',
        'elb_white_list_req': 'elbWhiteListReq',
        'public_bind_type': 'publicBindType',
        'eip_id': 'eipId'
    }

    def __init__(self, eip=None, elb_white_list_req=None, public_bind_type=None, eip_id=None):
        """CreateClusterPublicIpReq

        The model defined in huaweicloud sdk

        :param eip: 
        :type eip: :class:`huaweicloudsdkcss.v2.CreateClusterPublicEip`
        :param elb_white_list_req: 
        :type elb_white_list_req: :class:`huaweicloudsdkcss.v2.CreateClusterElbWhiteList`
        :param public_bind_type: 是否自动绑定弹性公网IP。auto_assign为自动分配，bind_existing为绑定已有IP，需要填写eipId字段。
        :type public_bind_type: str
        :param eip_id: 弹性公网IP的ID。
        :type eip_id: str
        """
        
        

        self._eip = None
        self._elb_white_list_req = None
        self._public_bind_type = None
        self._eip_id = None
        self.discriminator = None

        self.eip = eip
        self.elb_white_list_req = elb_white_list_req
        self.public_bind_type = public_bind_type
        if eip_id is not None:
            self.eip_id = eip_id

    @property
    def eip(self):
        """Gets the eip of this CreateClusterPublicIpReq.


        :return: The eip of this CreateClusterPublicIpReq.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterPublicEip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this CreateClusterPublicIpReq.


        :param eip: The eip of this CreateClusterPublicIpReq.
        :type eip: :class:`huaweicloudsdkcss.v2.CreateClusterPublicEip`
        """
        self._eip = eip

    @property
    def elb_white_list_req(self):
        """Gets the elb_white_list_req of this CreateClusterPublicIpReq.


        :return: The elb_white_list_req of this CreateClusterPublicIpReq.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterElbWhiteList`
        """
        return self._elb_white_list_req

    @elb_white_list_req.setter
    def elb_white_list_req(self, elb_white_list_req):
        """Sets the elb_white_list_req of this CreateClusterPublicIpReq.


        :param elb_white_list_req: The elb_white_list_req of this CreateClusterPublicIpReq.
        :type elb_white_list_req: :class:`huaweicloudsdkcss.v2.CreateClusterElbWhiteList`
        """
        self._elb_white_list_req = elb_white_list_req

    @property
    def public_bind_type(self):
        """Gets the public_bind_type of this CreateClusterPublicIpReq.

        是否自动绑定弹性公网IP。auto_assign为自动分配，bind_existing为绑定已有IP，需要填写eipId字段。

        :return: The public_bind_type of this CreateClusterPublicIpReq.
        :rtype: str
        """
        return self._public_bind_type

    @public_bind_type.setter
    def public_bind_type(self, public_bind_type):
        """Sets the public_bind_type of this CreateClusterPublicIpReq.

        是否自动绑定弹性公网IP。auto_assign为自动分配，bind_existing为绑定已有IP，需要填写eipId字段。

        :param public_bind_type: The public_bind_type of this CreateClusterPublicIpReq.
        :type public_bind_type: str
        """
        self._public_bind_type = public_bind_type

    @property
    def eip_id(self):
        """Gets the eip_id of this CreateClusterPublicIpReq.

        弹性公网IP的ID。

        :return: The eip_id of this CreateClusterPublicIpReq.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this CreateClusterPublicIpReq.

        弹性公网IP的ID。

        :param eip_id: The eip_id of this CreateClusterPublicIpReq.
        :type eip_id: str
        """
        self._eip_id = eip_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateClusterPublicIpReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
