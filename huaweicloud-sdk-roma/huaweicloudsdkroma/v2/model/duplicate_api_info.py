# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DuplicateApiInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'api_id': 'str',
        'api_name': 'str',
        'group_name': 'str',
        'group_id': 'str',
        'remark': 'str',
        'api_type': 'str'
    }

    attribute_map = {
        'api_id': 'api_id',
        'api_name': 'api_name',
        'group_name': 'group_name',
        'group_id': 'group_id',
        'remark': 'remark',
        'api_type': 'api_type'
    }

    def __init__(self, api_id=None, api_name=None, group_name=None, group_id=None, remark=None, api_type=None):
        """DuplicateApiInfo

        The model defined in huaweicloud sdk

        :param api_id: API ID
        :type api_id: str
        :param api_name: API名称
        :type api_name: str
        :param group_name: 分组名称
        :type group_name: str
        :param group_id: 分组ID
        :type group_id: str
        :param remark: API描述
        :type remark: str
        :param api_type: api类型： - self-owned：自有API - authorized：授权API
        :type api_type: str
        """
        
        

        self._api_id = None
        self._api_name = None
        self._group_name = None
        self._group_id = None
        self._remark = None
        self._api_type = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if remark is not None:
            self.remark = remark
        if api_type is not None:
            self.api_type = api_type

    @property
    def api_id(self):
        """Gets the api_id of this DuplicateApiInfo.

        API ID

        :return: The api_id of this DuplicateApiInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this DuplicateApiInfo.

        API ID

        :param api_id: The api_id of this DuplicateApiInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        """Gets the api_name of this DuplicateApiInfo.

        API名称

        :return: The api_name of this DuplicateApiInfo.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this DuplicateApiInfo.

        API名称

        :param api_name: The api_name of this DuplicateApiInfo.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def group_name(self):
        """Gets the group_name of this DuplicateApiInfo.

        分组名称

        :return: The group_name of this DuplicateApiInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this DuplicateApiInfo.

        分组名称

        :param group_name: The group_name of this DuplicateApiInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        """Gets the group_id of this DuplicateApiInfo.

        分组ID

        :return: The group_id of this DuplicateApiInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DuplicateApiInfo.

        分组ID

        :param group_id: The group_id of this DuplicateApiInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def remark(self):
        """Gets the remark of this DuplicateApiInfo.

        API描述

        :return: The remark of this DuplicateApiInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this DuplicateApiInfo.

        API描述

        :param remark: The remark of this DuplicateApiInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def api_type(self):
        """Gets the api_type of this DuplicateApiInfo.

        api类型： - self-owned：自有API - authorized：授权API

        :return: The api_type of this DuplicateApiInfo.
        :rtype: str
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this DuplicateApiInfo.

        api类型： - self-owned：自有API - authorized：授权API

        :param api_type: The api_type of this DuplicateApiInfo.
        :type api_type: str
        """
        self._api_type = api_type

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
        if not isinstance(other, DuplicateApiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
