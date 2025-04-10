# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProductTopicResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'int',
        'topic_id': 'str',
        'permission': 'int',
        'topic_name': 'str',
        'version': 'str',
        'description': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'topic_id': 'topic_id',
        'permission': 'permission',
        'topic_name': 'topic_name',
        'version': 'version',
        'description': 'description'
    }

    def __init__(self, product_id=None, topic_id=None, permission=None, topic_name=None, version=None, description=None):
        r"""CreateProductTopicResponse

        The model defined in huaweicloud sdk

        :param product_id: 归属产品ID
        :type product_id: int
        :param topic_id: 产品主题ID
        :type topic_id: str
        :param permission: 主题权限 0-发布 1-订阅
        :type permission: int
        :param topic_name: 主题名称
        :type topic_name: str
        :param version: 版本号
        :type version: str
        :param description: 描述
        :type description: str
        """
        
        super(CreateProductTopicResponse, self).__init__()

        self._product_id = None
        self._topic_id = None
        self._permission = None
        self._topic_name = None
        self._version = None
        self._description = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if topic_id is not None:
            self.topic_id = topic_id
        if permission is not None:
            self.permission = permission
        if topic_name is not None:
            self.topic_name = topic_name
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateProductTopicResponse.

        归属产品ID

        :return: The product_id of this CreateProductTopicResponse.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateProductTopicResponse.

        归属产品ID

        :param product_id: The product_id of this CreateProductTopicResponse.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def topic_id(self):
        r"""Gets the topic_id of this CreateProductTopicResponse.

        产品主题ID

        :return: The topic_id of this CreateProductTopicResponse.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        r"""Sets the topic_id of this CreateProductTopicResponse.

        产品主题ID

        :param topic_id: The topic_id of this CreateProductTopicResponse.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def permission(self):
        r"""Gets the permission of this CreateProductTopicResponse.

        主题权限 0-发布 1-订阅

        :return: The permission of this CreateProductTopicResponse.
        :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this CreateProductTopicResponse.

        主题权限 0-发布 1-订阅

        :param permission: The permission of this CreateProductTopicResponse.
        :type permission: int
        """
        self._permission = permission

    @property
    def topic_name(self):
        r"""Gets the topic_name of this CreateProductTopicResponse.

        主题名称

        :return: The topic_name of this CreateProductTopicResponse.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        r"""Sets the topic_name of this CreateProductTopicResponse.

        主题名称

        :param topic_name: The topic_name of this CreateProductTopicResponse.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def version(self):
        r"""Gets the version of this CreateProductTopicResponse.

        版本号

        :return: The version of this CreateProductTopicResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateProductTopicResponse.

        版本号

        :param version: The version of this CreateProductTopicResponse.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this CreateProductTopicResponse.

        描述

        :return: The description of this CreateProductTopicResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateProductTopicResponse.

        描述

        :param description: The description of this CreateProductTopicResponse.
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
        if not isinstance(other, CreateProductTopicResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
