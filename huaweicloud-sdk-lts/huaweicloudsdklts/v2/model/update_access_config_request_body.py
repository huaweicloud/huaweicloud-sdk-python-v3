# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccessConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_config_id': 'str',
        'access_config_detail': 'AccessConfigDeatil',
        'host_group_info': 'AccessConfigHostGroupIdList',
        'access_config_tag': 'list[AccessConfigTag]'
    }

    attribute_map = {
        'access_config_id': 'access_config_id',
        'access_config_detail': 'access_config_detail',
        'host_group_info': 'host_group_info',
        'access_config_tag': 'access_config_tag'
    }

    def __init__(self, access_config_id=None, access_config_detail=None, host_group_info=None, access_config_tag=None):
        """UpdateAccessConfigRequestBody

        The model defined in huaweicloud sdk

        :param access_config_id: 日志接入ID
        :type access_config_id: str
        :param access_config_detail: 
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatil`
        :param host_group_info: 
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        :param access_config_tag: 
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        
        

        self._access_config_id = None
        self._access_config_detail = None
        self._host_group_info = None
        self._access_config_tag = None
        self.discriminator = None

        self.access_config_id = access_config_id
        if access_config_detail is not None:
            self.access_config_detail = access_config_detail
        if host_group_info is not None:
            self.host_group_info = host_group_info
        if access_config_tag is not None:
            self.access_config_tag = access_config_tag

    @property
    def access_config_id(self):
        """Gets the access_config_id of this UpdateAccessConfigRequestBody.

        日志接入ID

        :return: The access_config_id of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_id

    @access_config_id.setter
    def access_config_id(self, access_config_id):
        """Sets the access_config_id of this UpdateAccessConfigRequestBody.

        日志接入ID

        :param access_config_id: The access_config_id of this UpdateAccessConfigRequestBody.
        :type access_config_id: str
        """
        self._access_config_id = access_config_id

    @property
    def access_config_detail(self):
        """Gets the access_config_detail of this UpdateAccessConfigRequestBody.

        :return: The access_config_detail of this UpdateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigDeatil`
        """
        return self._access_config_detail

    @access_config_detail.setter
    def access_config_detail(self, access_config_detail):
        """Sets the access_config_detail of this UpdateAccessConfigRequestBody.

        :param access_config_detail: The access_config_detail of this UpdateAccessConfigRequestBody.
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatil`
        """
        self._access_config_detail = access_config_detail

    @property
    def host_group_info(self):
        """Gets the host_group_info of this UpdateAccessConfigRequestBody.

        :return: The host_group_info of this UpdateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        """
        return self._host_group_info

    @host_group_info.setter
    def host_group_info(self, host_group_info):
        """Sets the host_group_info of this UpdateAccessConfigRequestBody.

        :param host_group_info: The host_group_info of this UpdateAccessConfigRequestBody.
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        """
        self._host_group_info = host_group_info

    @property
    def access_config_tag(self):
        """Gets the access_config_tag of this UpdateAccessConfigRequestBody.

        :return: The access_config_tag of this UpdateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        return self._access_config_tag

    @access_config_tag.setter
    def access_config_tag(self, access_config_tag):
        """Sets the access_config_tag of this UpdateAccessConfigRequestBody.

        :param access_config_tag: The access_config_tag of this UpdateAccessConfigRequestBody.
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        self._access_config_tag = access_config_tag

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
        if not isinstance(other, UpdateAccessConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
