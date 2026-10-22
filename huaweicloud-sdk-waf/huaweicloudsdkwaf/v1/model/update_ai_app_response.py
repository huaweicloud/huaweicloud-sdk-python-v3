# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAiAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'name': 'str',
        'description': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'app_id': 'appId',
        'name': 'name',
        'description': 'description',
        'update_time': 'updateTime'
    }

    def __init__(self, app_id=None, name=None, description=None, update_time=None):
        r"""UpdateAiAppResponse

        The model defined in huaweicloud sdk

        :param app_id: AI应用ID
        :type app_id: str
        :param name: AI应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param update_time: 更新时间戳（毫秒Unix时间戳）
        :type update_time: int
        """
        
        super().__init__()

        self._app_id = None
        self._name = None
        self._description = None
        self._update_time = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if update_time is not None:
            self.update_time = update_time

    @property
    def app_id(self):
        r"""Gets the app_id of this UpdateAiAppResponse.

        AI应用ID

        :return: The app_id of this UpdateAiAppResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this UpdateAiAppResponse.

        AI应用ID

        :param app_id: The app_id of this UpdateAiAppResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def name(self):
        r"""Gets the name of this UpdateAiAppResponse.

        AI应用名称

        :return: The name of this UpdateAiAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateAiAppResponse.

        AI应用名称

        :param name: The name of this UpdateAiAppResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateAiAppResponse.

        应用描述

        :return: The description of this UpdateAiAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAiAppResponse.

        应用描述

        :param description: The description of this UpdateAiAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateAiAppResponse.

        更新时间戳（毫秒Unix时间戳）

        :return: The update_time of this UpdateAiAppResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateAiAppResponse.

        更新时间戳（毫秒Unix时间戳）

        :param update_time: The update_time of this UpdateAiAppResponse.
        :type update_time: int
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("UpdateAiAppResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateAiAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
