# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppResponse(SdkResponse):

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
        'description': 'str',
        'app_type': 'str',
        'provider_type': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'description': 'description',
        'app_type': 'app_type',
        'provider_type': 'provider_type',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, app_id=None, description=None, app_type=None, provider_type=None, create_time=None, update_time=None):
        """ShowAppResponse

        The model defined in huaweicloud sdk

        :param app_id: 应用模板ID
        :type app_id: str
        :param description: 应用描述
        :type description: str
        :param app_type: 应用类型
        :type app_type: str
        :param provider_type: 应用来源
        :type provider_type: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        """
        
        super(ShowAppResponse, self).__init__()

        self._app_id = None
        self._description = None
        self._app_type = None
        self._provider_type = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if description is not None:
            self.description = description
        if app_type is not None:
            self.app_type = app_type
        if provider_type is not None:
            self.provider_type = provider_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def app_id(self):
        """Gets the app_id of this ShowAppResponse.

        应用模板ID

        :return: The app_id of this ShowAppResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowAppResponse.

        应用模板ID

        :param app_id: The app_id of this ShowAppResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def description(self):
        """Gets the description of this ShowAppResponse.

        应用描述

        :return: The description of this ShowAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowAppResponse.

        应用描述

        :param description: The description of this ShowAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def app_type(self):
        """Gets the app_type of this ShowAppResponse.

        应用类型

        :return: The app_type of this ShowAppResponse.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ShowAppResponse.

        应用类型

        :param app_type: The app_type of this ShowAppResponse.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def provider_type(self):
        """Gets the provider_type of this ShowAppResponse.

        应用来源

        :return: The provider_type of this ShowAppResponse.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ShowAppResponse.

        应用来源

        :param provider_type: The provider_type of this ShowAppResponse.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def create_time(self):
        """Gets the create_time of this ShowAppResponse.

        创建时间

        :return: The create_time of this ShowAppResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAppResponse.

        创建时间

        :param create_time: The create_time of this ShowAppResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowAppResponse.

        最后一次修改时间

        :return: The update_time of this ShowAppResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowAppResponse.

        最后一次修改时间

        :param update_time: The update_time of this ShowAppResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
