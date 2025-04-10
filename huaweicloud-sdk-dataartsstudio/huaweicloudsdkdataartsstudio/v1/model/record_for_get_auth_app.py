# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordForGetAuthApp:

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
        'app_name': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'api_using_time': 'int',
        'approval_time': 'int',
        'relationship_type': 'str',
        'static_params': 'list[StaticParam]'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'api_using_time': 'api_using_time',
        'approval_time': 'approval_time',
        'relationship_type': 'relationship_type',
        'static_params': 'static_params'
    }

    def __init__(self, app_id=None, app_name=None, instance_id=None, instance_name=None, api_using_time=None, approval_time=None, relationship_type=None, static_params=None):
        r"""RecordForGetAuthApp

        The model defined in huaweicloud sdk

        :param app_id: 应用编号
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param instance_id: 集群实例id
        :type instance_id: str
        :param instance_name: 集群实例名称
        :type instance_name: str
        :param api_using_time: 使用截止时间
        :type api_using_time: int
        :param approval_time: 授权时间
        :type approval_time: int
        :param relationship_type: 绑定关系
        :type relationship_type: str
        :param static_params: 静态参数列表
        :type static_params: list[:class:`huaweicloudsdkdataartsstudio.v1.StaticParam`]
        """
        
        

        self._app_id = None
        self._app_name = None
        self._instance_id = None
        self._instance_name = None
        self._api_using_time = None
        self._approval_time = None
        self._relationship_type = None
        self._static_params = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if api_using_time is not None:
            self.api_using_time = api_using_time
        if approval_time is not None:
            self.approval_time = approval_time
        if relationship_type is not None:
            self.relationship_type = relationship_type
        if static_params is not None:
            self.static_params = static_params

    @property
    def app_id(self):
        r"""Gets the app_id of this RecordForGetAuthApp.

        应用编号

        :return: The app_id of this RecordForGetAuthApp.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this RecordForGetAuthApp.

        应用编号

        :param app_id: The app_id of this RecordForGetAuthApp.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this RecordForGetAuthApp.

        应用名称

        :return: The app_name of this RecordForGetAuthApp.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this RecordForGetAuthApp.

        应用名称

        :param app_name: The app_name of this RecordForGetAuthApp.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RecordForGetAuthApp.

        集群实例id

        :return: The instance_id of this RecordForGetAuthApp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RecordForGetAuthApp.

        集群实例id

        :param instance_id: The instance_id of this RecordForGetAuthApp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this RecordForGetAuthApp.

        集群实例名称

        :return: The instance_name of this RecordForGetAuthApp.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this RecordForGetAuthApp.

        集群实例名称

        :param instance_name: The instance_name of this RecordForGetAuthApp.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def api_using_time(self):
        r"""Gets the api_using_time of this RecordForGetAuthApp.

        使用截止时间

        :return: The api_using_time of this RecordForGetAuthApp.
        :rtype: int
        """
        return self._api_using_time

    @api_using_time.setter
    def api_using_time(self, api_using_time):
        r"""Sets the api_using_time of this RecordForGetAuthApp.

        使用截止时间

        :param api_using_time: The api_using_time of this RecordForGetAuthApp.
        :type api_using_time: int
        """
        self._api_using_time = api_using_time

    @property
    def approval_time(self):
        r"""Gets the approval_time of this RecordForGetAuthApp.

        授权时间

        :return: The approval_time of this RecordForGetAuthApp.
        :rtype: int
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        r"""Sets the approval_time of this RecordForGetAuthApp.

        授权时间

        :param approval_time: The approval_time of this RecordForGetAuthApp.
        :type approval_time: int
        """
        self._approval_time = approval_time

    @property
    def relationship_type(self):
        r"""Gets the relationship_type of this RecordForGetAuthApp.

        绑定关系

        :return: The relationship_type of this RecordForGetAuthApp.
        :rtype: str
        """
        return self._relationship_type

    @relationship_type.setter
    def relationship_type(self, relationship_type):
        r"""Sets the relationship_type of this RecordForGetAuthApp.

        绑定关系

        :param relationship_type: The relationship_type of this RecordForGetAuthApp.
        :type relationship_type: str
        """
        self._relationship_type = relationship_type

    @property
    def static_params(self):
        r"""Gets the static_params of this RecordForGetAuthApp.

        静态参数列表

        :return: The static_params of this RecordForGetAuthApp.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.StaticParam`]
        """
        return self._static_params

    @static_params.setter
    def static_params(self, static_params):
        r"""Sets the static_params of this RecordForGetAuthApp.

        静态参数列表

        :param static_params: The static_params of this RecordForGetAuthApp.
        :type static_params: list[:class:`huaweicloudsdkdataartsstudio.v1.StaticParam`]
        """
        self._static_params = static_params

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
        if not isinstance(other, RecordForGetAuthApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
