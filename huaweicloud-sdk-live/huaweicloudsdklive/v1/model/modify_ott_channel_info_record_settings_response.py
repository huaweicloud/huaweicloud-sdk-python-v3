# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyOttChannelInfoRecordSettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_code': 'str',
        'result_msg': 'str',
        'domain': 'str',
        'app_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'result_code': 'result_code',
        'result_msg': 'result_msg',
        'domain': 'domain',
        'app_name': 'app_name',
        'id': 'id'
    }

    def __init__(self, result_code=None, result_msg=None, domain=None, app_name=None, id=None):
        r"""ModifyOttChannelInfoRecordSettingsResponse

        The model defined in huaweicloud sdk

        :param result_code: 错误码
        :type result_code: str
        :param result_msg: 错误描述
        :type result_msg: str
        :param domain: 推流域名
        :type domain: str
        :param app_name: 组名或应用名，为必填项
        :type app_name: str
        :param id: 频道ID。频道唯一标识，为必填项
        :type id: str
        """
        
        super(ModifyOttChannelInfoRecordSettingsResponse, self).__init__()

        self._result_code = None
        self._result_msg = None
        self._domain = None
        self._app_name = None
        self._id = None
        self.discriminator = None

        if result_code is not None:
            self.result_code = result_code
        if result_msg is not None:
            self.result_msg = result_msg
        if domain is not None:
            self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if id is not None:
            self.id = id

    @property
    def result_code(self):
        r"""Gets the result_code of this ModifyOttChannelInfoRecordSettingsResponse.

        错误码

        :return: The result_code of this ModifyOttChannelInfoRecordSettingsResponse.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this ModifyOttChannelInfoRecordSettingsResponse.

        错误码

        :param result_code: The result_code of this ModifyOttChannelInfoRecordSettingsResponse.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def result_msg(self):
        r"""Gets the result_msg of this ModifyOttChannelInfoRecordSettingsResponse.

        错误描述

        :return: The result_msg of this ModifyOttChannelInfoRecordSettingsResponse.
        :rtype: str
        """
        return self._result_msg

    @result_msg.setter
    def result_msg(self, result_msg):
        r"""Sets the result_msg of this ModifyOttChannelInfoRecordSettingsResponse.

        错误描述

        :param result_msg: The result_msg of this ModifyOttChannelInfoRecordSettingsResponse.
        :type result_msg: str
        """
        self._result_msg = result_msg

    @property
    def domain(self):
        r"""Gets the domain of this ModifyOttChannelInfoRecordSettingsResponse.

        推流域名

        :return: The domain of this ModifyOttChannelInfoRecordSettingsResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ModifyOttChannelInfoRecordSettingsResponse.

        推流域名

        :param domain: The domain of this ModifyOttChannelInfoRecordSettingsResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this ModifyOttChannelInfoRecordSettingsResponse.

        组名或应用名，为必填项

        :return: The app_name of this ModifyOttChannelInfoRecordSettingsResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ModifyOttChannelInfoRecordSettingsResponse.

        组名或应用名，为必填项

        :param app_name: The app_name of this ModifyOttChannelInfoRecordSettingsResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this ModifyOttChannelInfoRecordSettingsResponse.

        频道ID。频道唯一标识，为必填项

        :return: The id of this ModifyOttChannelInfoRecordSettingsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModifyOttChannelInfoRecordSettingsResponse.

        频道ID。频道唯一标识，为必填项

        :param id: The id of this ModifyOttChannelInfoRecordSettingsResponse.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ModifyOttChannelInfoRecordSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
