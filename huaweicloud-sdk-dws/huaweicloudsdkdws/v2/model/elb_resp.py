# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElbResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_ip': 'str',
        'private_ip': 'str',
        'private_endpoint': 'str',
        'name': 'str',
        'id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'private_endpoint': 'private_endpoint',
        'name': 'name',
        'id': 'id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, public_ip=None, private_ip=None, private_endpoint=None, name=None, id=None, vpc_id=None):
        r"""ElbResp

        The model defined in huaweicloud sdk

        :param public_ip: **参数解释**： 公网ip。 **取值范围**： 有效的公网ipv4地址。
        :type public_ip: str
        :param private_ip: **参数解释**： 内网ip。 **取值范围**： 有效的内网ipv4地址。
        :type private_ip: str
        :param private_endpoint: **参数解释**： Elb终端地址。 **取值范围**： 不涉及。
        :type private_endpoint: str
        :param name: **参数解释**： Elb名称。 **取值范围**： 不涉及。
        :type name: str
        :param id: **参数解释**： Elb的ID。 **取值范围**： 不涉及。
        :type id: str
        :param vpc_id: **参数解释**： Elb所属VPC的ID。 **取值范围**： 不涉及。
        :type vpc_id: str
        """
        
        

        self._public_ip = None
        self._private_ip = None
        self._private_endpoint = None
        self._name = None
        self._id = None
        self._vpc_id = None
        self.discriminator = None

        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if private_endpoint is not None:
            self.private_endpoint = private_endpoint
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ElbResp.

        **参数解释**： 公网ip。 **取值范围**： 有效的公网ipv4地址。

        :return: The public_ip of this ElbResp.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ElbResp.

        **参数解释**： 公网ip。 **取值范围**： 有效的公网ipv4地址。

        :param public_ip: The public_ip of this ElbResp.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ElbResp.

        **参数解释**： 内网ip。 **取值范围**： 有效的内网ipv4地址。

        :return: The private_ip of this ElbResp.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ElbResp.

        **参数解释**： 内网ip。 **取值范围**： 有效的内网ipv4地址。

        :param private_ip: The private_ip of this ElbResp.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def private_endpoint(self):
        r"""Gets the private_endpoint of this ElbResp.

        **参数解释**： Elb终端地址。 **取值范围**： 不涉及。

        :return: The private_endpoint of this ElbResp.
        :rtype: str
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        r"""Sets the private_endpoint of this ElbResp.

        **参数解释**： Elb终端地址。 **取值范围**： 不涉及。

        :param private_endpoint: The private_endpoint of this ElbResp.
        :type private_endpoint: str
        """
        self._private_endpoint = private_endpoint

    @property
    def name(self):
        r"""Gets the name of this ElbResp.

        **参数解释**： Elb名称。 **取值范围**： 不涉及。

        :return: The name of this ElbResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ElbResp.

        **参数解释**： Elb名称。 **取值范围**： 不涉及。

        :param name: The name of this ElbResp.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ElbResp.

        **参数解释**： Elb的ID。 **取值范围**： 不涉及。

        :return: The id of this ElbResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ElbResp.

        **参数解释**： Elb的ID。 **取值范围**： 不涉及。

        :param id: The id of this ElbResp.
        :type id: str
        """
        self._id = id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ElbResp.

        **参数解释**： Elb所属VPC的ID。 **取值范围**： 不涉及。

        :return: The vpc_id of this ElbResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ElbResp.

        **参数解释**： Elb所属VPC的ID。 **取值范围**： 不涉及。

        :param vpc_id: The vpc_id of this ElbResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ElbResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
