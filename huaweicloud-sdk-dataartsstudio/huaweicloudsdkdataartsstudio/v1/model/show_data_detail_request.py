# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'guid': 'str',
        'ignore_relationships': 'bool'
    }

    attribute_map = {
        'instance': 'instance',
        'guid': 'guid',
        'ignore_relationships': 'ignore_relationships'
    }

    def __init__(self, instance=None, guid=None, ignore_relationships=None):
        """ShowDataDetailRequest

        The model defined in huaweicloud sdk

        :param instance: 实例id
        :type instance: str
        :param guid: 资产guid
        :type guid: str
        :param ignore_relationships: 是否忽略关联资产 缺省值：false
        :type ignore_relationships: bool
        """
        
        

        self._instance = None
        self._guid = None
        self._ignore_relationships = None
        self.discriminator = None

        self.instance = instance
        self.guid = guid
        if ignore_relationships is not None:
            self.ignore_relationships = ignore_relationships

    @property
    def instance(self):
        """Gets the instance of this ShowDataDetailRequest.

        实例id

        :return: The instance of this ShowDataDetailRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ShowDataDetailRequest.

        实例id

        :param instance: The instance of this ShowDataDetailRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def guid(self):
        """Gets the guid of this ShowDataDetailRequest.

        资产guid

        :return: The guid of this ShowDataDetailRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this ShowDataDetailRequest.

        资产guid

        :param guid: The guid of this ShowDataDetailRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def ignore_relationships(self):
        """Gets the ignore_relationships of this ShowDataDetailRequest.

        是否忽略关联资产 缺省值：false

        :return: The ignore_relationships of this ShowDataDetailRequest.
        :rtype: bool
        """
        return self._ignore_relationships

    @ignore_relationships.setter
    def ignore_relationships(self, ignore_relationships):
        """Sets the ignore_relationships of this ShowDataDetailRequest.

        是否忽略关联资产 缺省值：false

        :param ignore_relationships: The ignore_relationships of this ShowDataDetailRequest.
        :type ignore_relationships: bool
        """
        self._ignore_relationships = ignore_relationships

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
        if not isinstance(other, ShowDataDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
