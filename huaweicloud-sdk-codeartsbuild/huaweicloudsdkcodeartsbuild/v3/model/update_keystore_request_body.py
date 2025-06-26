# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeystoreRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'description': 'str',
        'keystore_name': 'str',
        'share': 'int'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'keystore_name': 'keystore_name',
        'share': 'share'
    }

    def __init__(self, id=None, description=None, keystore_name=None, share=None):
        r"""UpdateKeystoreRequestBody

        The model defined in huaweicloud sdk

        :param id: 文件ID
        :type id: str
        :param description: 文件描述
        :type description: str
        :param keystore_name: 文件名
        :type keystore_name: str
        :param share: 是否租户内共享，1-共享，0-不共享
        :type share: int
        """
        
        

        self._id = None
        self._description = None
        self._keystore_name = None
        self._share = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.keystore_name = keystore_name
        self.share = share

    @property
    def id(self):
        r"""Gets the id of this UpdateKeystoreRequestBody.

        文件ID

        :return: The id of this UpdateKeystoreRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateKeystoreRequestBody.

        文件ID

        :param id: The id of this UpdateKeystoreRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this UpdateKeystoreRequestBody.

        文件描述

        :return: The description of this UpdateKeystoreRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateKeystoreRequestBody.

        文件描述

        :param description: The description of this UpdateKeystoreRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def keystore_name(self):
        r"""Gets the keystore_name of this UpdateKeystoreRequestBody.

        文件名

        :return: The keystore_name of this UpdateKeystoreRequestBody.
        :rtype: str
        """
        return self._keystore_name

    @keystore_name.setter
    def keystore_name(self, keystore_name):
        r"""Sets the keystore_name of this UpdateKeystoreRequestBody.

        文件名

        :param keystore_name: The keystore_name of this UpdateKeystoreRequestBody.
        :type keystore_name: str
        """
        self._keystore_name = keystore_name

    @property
    def share(self):
        r"""Gets the share of this UpdateKeystoreRequestBody.

        是否租户内共享，1-共享，0-不共享

        :return: The share of this UpdateKeystoreRequestBody.
        :rtype: int
        """
        return self._share

    @share.setter
    def share(self, share):
        r"""Sets the share of this UpdateKeystoreRequestBody.

        是否租户内共享，1-共享，0-不共享

        :param share: The share of this UpdateKeystoreRequestBody.
        :type share: int
        """
        self._share = share

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
        if not isinstance(other, UpdateKeystoreRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
