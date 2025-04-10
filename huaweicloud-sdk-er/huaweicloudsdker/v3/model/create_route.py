# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRoute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination': 'str',
        'attachment_id': 'str',
        'is_blackhole': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'attachment_id': 'attachment_id',
        'is_blackhole': 'is_blackhole',
        'description': 'description'
    }

    def __init__(self, destination=None, attachment_id=None, is_blackhole=None, description=None):
        r"""CreateRoute

        The model defined in huaweicloud sdk

        :param destination: 路由目的地址
        :type destination: str
        :param attachment_id: 路由下一跳指向的连接ID
        :type attachment_id: str
        :param is_blackhole: 是否为黑洞路由，默认为false
        :type is_blackhole: bool
        :param description: 路由描述信息
        :type description: str
        """
        
        

        self._destination = None
        self._attachment_id = None
        self._is_blackhole = None
        self._description = None
        self.discriminator = None

        self.destination = destination
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if is_blackhole is not None:
            self.is_blackhole = is_blackhole
        if description is not None:
            self.description = description

    @property
    def destination(self):
        r"""Gets the destination of this CreateRoute.

        路由目的地址

        :return: The destination of this CreateRoute.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this CreateRoute.

        路由目的地址

        :param destination: The destination of this CreateRoute.
        :type destination: str
        """
        self._destination = destination

    @property
    def attachment_id(self):
        r"""Gets the attachment_id of this CreateRoute.

        路由下一跳指向的连接ID

        :return: The attachment_id of this CreateRoute.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        r"""Sets the attachment_id of this CreateRoute.

        路由下一跳指向的连接ID

        :param attachment_id: The attachment_id of this CreateRoute.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

    @property
    def is_blackhole(self):
        r"""Gets the is_blackhole of this CreateRoute.

        是否为黑洞路由，默认为false

        :return: The is_blackhole of this CreateRoute.
        :rtype: bool
        """
        return self._is_blackhole

    @is_blackhole.setter
    def is_blackhole(self, is_blackhole):
        r"""Sets the is_blackhole of this CreateRoute.

        是否为黑洞路由，默认为false

        :param is_blackhole: The is_blackhole of this CreateRoute.
        :type is_blackhole: bool
        """
        self._is_blackhole = is_blackhole

    @property
    def description(self):
        r"""Gets the description of this CreateRoute.

        路由描述信息

        :return: The description of this CreateRoute.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateRoute.

        路由描述信息

        :param description: The description of this CreateRoute.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
