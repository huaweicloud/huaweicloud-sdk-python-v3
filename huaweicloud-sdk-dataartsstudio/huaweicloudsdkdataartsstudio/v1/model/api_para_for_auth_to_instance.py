# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiParaForAuthToInstance:

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
        'instance_id': 'str',
        'app_id': 'str',
        'apply_type': 'str',
        'time': 'str'
    }

    attribute_map = {
        'api_id': 'api_id',
        'instance_id': 'instance_id',
        'app_id': 'app_id',
        'apply_type': 'apply_type',
        'time': 'time'
    }

    def __init__(self, api_id=None, instance_id=None, app_id=None, apply_type=None, time=None):
        """ApiParaForAuthToInstance

        The model defined in huaweicloud sdk

        :param api_id: api编号
        :type api_id: str
        :param instance_id: 集群编号
        :type instance_id: str
        :param app_id: app编号
        :type app_id: str
        :param apply_type: 申请类型
        :type apply_type: str
        :param time: 截止时间
        :type time: str
        """
        
        

        self._api_id = None
        self._instance_id = None
        self._app_id = None
        self._apply_type = None
        self._time = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if instance_id is not None:
            self.instance_id = instance_id
        if app_id is not None:
            self.app_id = app_id
        if apply_type is not None:
            self.apply_type = apply_type
        if time is not None:
            self.time = time

    @property
    def api_id(self):
        """Gets the api_id of this ApiParaForAuthToInstance.

        api编号

        :return: The api_id of this ApiParaForAuthToInstance.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ApiParaForAuthToInstance.

        api编号

        :param api_id: The api_id of this ApiParaForAuthToInstance.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ApiParaForAuthToInstance.

        集群编号

        :return: The instance_id of this ApiParaForAuthToInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ApiParaForAuthToInstance.

        集群编号

        :param instance_id: The instance_id of this ApiParaForAuthToInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        """Gets the app_id of this ApiParaForAuthToInstance.

        app编号

        :return: The app_id of this ApiParaForAuthToInstance.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ApiParaForAuthToInstance.

        app编号

        :param app_id: The app_id of this ApiParaForAuthToInstance.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def apply_type(self):
        """Gets the apply_type of this ApiParaForAuthToInstance.

        申请类型

        :return: The apply_type of this ApiParaForAuthToInstance.
        :rtype: str
        """
        return self._apply_type

    @apply_type.setter
    def apply_type(self, apply_type):
        """Sets the apply_type of this ApiParaForAuthToInstance.

        申请类型

        :param apply_type: The apply_type of this ApiParaForAuthToInstance.
        :type apply_type: str
        """
        self._apply_type = apply_type

    @property
    def time(self):
        """Gets the time of this ApiParaForAuthToInstance.

        截止时间

        :return: The time of this ApiParaForAuthToInstance.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ApiParaForAuthToInstance.

        截止时间

        :param time: The time of this ApiParaForAuthToInstance.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, ApiParaForAuthToInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
