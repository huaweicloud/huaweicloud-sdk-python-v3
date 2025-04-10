# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessoryUrl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accessory_id': 'str',
        'accessory_name': 'str',
        'accessory_url': 'str'
    }

    attribute_map = {
        'accessory_id': 'accessory_id',
        'accessory_name': 'accessory_name',
        'accessory_url': 'accessory_url'
    }

    def __init__(self, accessory_id=None, accessory_name=None, accessory_url=None):
        r"""AccessoryUrl

        The model defined in huaweicloud sdk

        :param accessory_id: 附件id
        :type accessory_id: str
        :param accessory_name: 文件名称
        :type accessory_name: str
        :param accessory_url: 附件链接
        :type accessory_url: str
        """
        
        

        self._accessory_id = None
        self._accessory_name = None
        self._accessory_url = None
        self.discriminator = None

        if accessory_id is not None:
            self.accessory_id = accessory_id
        if accessory_name is not None:
            self.accessory_name = accessory_name
        if accessory_url is not None:
            self.accessory_url = accessory_url

    @property
    def accessory_id(self):
        r"""Gets the accessory_id of this AccessoryUrl.

        附件id

        :return: The accessory_id of this AccessoryUrl.
        :rtype: str
        """
        return self._accessory_id

    @accessory_id.setter
    def accessory_id(self, accessory_id):
        r"""Sets the accessory_id of this AccessoryUrl.

        附件id

        :param accessory_id: The accessory_id of this AccessoryUrl.
        :type accessory_id: str
        """
        self._accessory_id = accessory_id

    @property
    def accessory_name(self):
        r"""Gets the accessory_name of this AccessoryUrl.

        文件名称

        :return: The accessory_name of this AccessoryUrl.
        :rtype: str
        """
        return self._accessory_name

    @accessory_name.setter
    def accessory_name(self, accessory_name):
        r"""Sets the accessory_name of this AccessoryUrl.

        文件名称

        :param accessory_name: The accessory_name of this AccessoryUrl.
        :type accessory_name: str
        """
        self._accessory_name = accessory_name

    @property
    def accessory_url(self):
        r"""Gets the accessory_url of this AccessoryUrl.

        附件链接

        :return: The accessory_url of this AccessoryUrl.
        :rtype: str
        """
        return self._accessory_url

    @accessory_url.setter
    def accessory_url(self, accessory_url):
        r"""Sets the accessory_url of this AccessoryUrl.

        附件链接

        :param accessory_url: The accessory_url of this AccessoryUrl.
        :type accessory_url: str
        """
        self._accessory_url = accessory_url

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
        if not isinstance(other, AccessoryUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
