# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceParamRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, x_language=None):
        """ShowInstanceParamRequest

        The model defined in huaweicloud sdk

        :param instance_id: DDM实例ID
        :type instance_id: str
        :param offset: 分页参数：起始值 [大于等于0] 。默认值是0。
        :type offset: int
        :param limit: 分页参数：每页多少条 [大于0且小于等于128]。默认值是128。
        :type limit: int
        :param x_language: 语种，默认中文。中文:zh-cn;英文:en-us
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowInstanceParamRequest.

        DDM实例ID

        :return: The instance_id of this ShowInstanceParamRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowInstanceParamRequest.

        DDM实例ID

        :param instance_id: The instance_id of this ShowInstanceParamRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ShowInstanceParamRequest.

        分页参数：起始值 [大于等于0] 。默认值是0。

        :return: The offset of this ShowInstanceParamRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowInstanceParamRequest.

        分页参数：起始值 [大于等于0] 。默认值是0。

        :param offset: The offset of this ShowInstanceParamRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowInstanceParamRequest.

        分页参数：每页多少条 [大于0且小于等于128]。默认值是128。

        :return: The limit of this ShowInstanceParamRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowInstanceParamRequest.

        分页参数：每页多少条 [大于0且小于等于128]。默认值是128。

        :param limit: The limit of this ShowInstanceParamRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ShowInstanceParamRequest.

        语种，默认中文。中文:zh-cn;英文:en-us

        :return: The x_language of this ShowInstanceParamRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowInstanceParamRequest.

        语种，默认中文。中文:zh-cn;英文:en-us

        :param x_language: The x_language of this ShowInstanceParamRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowInstanceParamRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
