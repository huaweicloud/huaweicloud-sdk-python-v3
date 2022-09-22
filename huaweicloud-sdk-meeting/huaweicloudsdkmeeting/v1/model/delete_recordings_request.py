# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRecordingsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conf_uui_ds': 'str',
        'user_uuid': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'conf_uui_ds': 'confUUIDs',
        'user_uuid': 'userUUID',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, conf_uui_ds=None, user_uuid=None, x_authorization_type=None, x_site_id=None):
        """DeleteRecordingsRequest

        The model defined in huaweicloud sdk

        :param conf_uui_ds: 会议UUID列表，多个会议UUID之间以英文逗号隔开。
        :type conf_uui_ds: str
        :param user_uuid: 用户的UUID。 &gt; 该参数将废弃，请勿使用。 
        :type user_uuid: str
        :param x_authorization_type: 标识是否为第三方portal过来的请求。 &gt; 该参数将废弃，请勿使用。 
        :type x_authorization_type: str
        :param x_site_id: 用于区分到哪个HCSO站点鉴权。 &gt; 该参数将废弃，请勿使用。 
        :type x_site_id: str
        """
        
        

        self._conf_uui_ds = None
        self._user_uuid = None
        self._x_authorization_type = None
        self._x_site_id = None
        self.discriminator = None

        self.conf_uui_ds = conf_uui_ds
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def conf_uui_ds(self):
        """Gets the conf_uui_ds of this DeleteRecordingsRequest.

        会议UUID列表，多个会议UUID之间以英文逗号隔开。

        :return: The conf_uui_ds of this DeleteRecordingsRequest.
        :rtype: str
        """
        return self._conf_uui_ds

    @conf_uui_ds.setter
    def conf_uui_ds(self, conf_uui_ds):
        """Sets the conf_uui_ds of this DeleteRecordingsRequest.

        会议UUID列表，多个会议UUID之间以英文逗号隔开。

        :param conf_uui_ds: The conf_uui_ds of this DeleteRecordingsRequest.
        :type conf_uui_ds: str
        """
        self._conf_uui_ds = conf_uui_ds

    @property
    def user_uuid(self):
        """Gets the user_uuid of this DeleteRecordingsRequest.

        用户的UUID。 > 该参数将废弃，请勿使用。 

        :return: The user_uuid of this DeleteRecordingsRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this DeleteRecordingsRequest.

        用户的UUID。 > 该参数将废弃，请勿使用。 

        :param user_uuid: The user_uuid of this DeleteRecordingsRequest.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this DeleteRecordingsRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :return: The x_authorization_type of this DeleteRecordingsRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this DeleteRecordingsRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :param x_authorization_type: The x_authorization_type of this DeleteRecordingsRequest.
        :type x_authorization_type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this DeleteRecordingsRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :return: The x_site_id of this DeleteRecordingsRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this DeleteRecordingsRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :param x_site_id: The x_site_id of this DeleteRecordingsRequest.
        :type x_site_id: str
        """
        self._x_site_id = x_site_id

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
        if not isinstance(other, DeleteRecordingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
