# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddAppIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('app_key')

    openapi_types = {
        'app_name': 'str',
        'app_id': 'str',
        'app_key': 'str',
        'description': 'str',
        'create_time': 'str',
        'last_update_time': 'str',
        'status': 'int'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_id': 'app_id',
        'app_key': 'app_key',
        'description': 'description',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time',
        'status': 'status'
    }

    def __init__(self, app_name=None, app_id=None, app_key=None, description=None, create_time=None, last_update_time=None, status=None):
        r"""AddAppIdResponse

        The model defined in huaweicloud sdk

        :param app_name: 企业应用名称
        :type app_name: str
        :param app_id: 企业应用ID
        :type app_id: str
        :param app_key: 企业应用appkey
        :type app_key: str
        :param description: 企业应用描述
        :type description: str
        :param create_time: 企业应用创建时间
        :type create_time: str
        :param last_update_time: 最近修改时间
        :type last_update_time: str
        :param status: 企业应用状态  * 0：正常  * 1：停用 
        :type status: int
        """
        
        super(AddAppIdResponse, self).__init__()

        self._app_name = None
        self._app_id = None
        self._app_key = None
        self._description = None
        self._create_time = None
        self._last_update_time = None
        self._status = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_id is not None:
            self.app_id = app_id
        if app_key is not None:
            self.app_key = app_key
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if status is not None:
            self.status = status

    @property
    def app_name(self):
        r"""Gets the app_name of this AddAppIdResponse.

        企业应用名称

        :return: The app_name of this AddAppIdResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this AddAppIdResponse.

        企业应用名称

        :param app_name: The app_name of this AddAppIdResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        r"""Gets the app_id of this AddAppIdResponse.

        企业应用ID

        :return: The app_id of this AddAppIdResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AddAppIdResponse.

        企业应用ID

        :param app_id: The app_id of this AddAppIdResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_key(self):
        r"""Gets the app_key of this AddAppIdResponse.

        企业应用appkey

        :return: The app_key of this AddAppIdResponse.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this AddAppIdResponse.

        企业应用appkey

        :param app_key: The app_key of this AddAppIdResponse.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def description(self):
        r"""Gets the description of this AddAppIdResponse.

        企业应用描述

        :return: The description of this AddAppIdResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddAppIdResponse.

        企业应用描述

        :param description: The description of this AddAppIdResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this AddAppIdResponse.

        企业应用创建时间

        :return: The create_time of this AddAppIdResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AddAppIdResponse.

        企业应用创建时间

        :param create_time: The create_time of this AddAppIdResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this AddAppIdResponse.

        最近修改时间

        :return: The last_update_time of this AddAppIdResponse.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this AddAppIdResponse.

        最近修改时间

        :param last_update_time: The last_update_time of this AddAppIdResponse.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def status(self):
        r"""Gets the status of this AddAppIdResponse.

        企业应用状态  * 0：正常  * 1：停用 

        :return: The status of this AddAppIdResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AddAppIdResponse.

        企业应用状态  * 0：正常  * 1：停用 

        :param status: The status of this AddAppIdResponse.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, AddAppIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
