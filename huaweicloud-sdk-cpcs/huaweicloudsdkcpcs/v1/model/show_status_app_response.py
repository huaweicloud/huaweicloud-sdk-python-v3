# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'app_list': 'list[ShowStatusAppItem]',
        'total_access_count': 'int',
        'success_access_count': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'app_list': 'app_list',
        'total_access_count': 'total_access_count',
        'success_access_count': 'success_access_count'
    }

    def __init__(self, metric_name=None, app_list=None, total_access_count=None, success_access_count=None):
        r"""ShowStatusAppResponse

        The model defined in huaweicloud sdk

        :param metric_name: 资源名称
        :type metric_name: str
        :param app_list: 应用列表
        :type app_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusAppItem`]
        :param total_access_count: 总访问次数
        :type total_access_count: int
        :param success_access_count: 成功访问次数
        :type success_access_count: int
        """
        
        super().__init__()

        self._metric_name = None
        self._app_list = None
        self._total_access_count = None
        self._success_access_count = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if app_list is not None:
            self.app_list = app_list
        if total_access_count is not None:
            self.total_access_count = total_access_count
        if success_access_count is not None:
            self.success_access_count = success_access_count

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowStatusAppResponse.

        资源名称

        :return: The metric_name of this ShowStatusAppResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowStatusAppResponse.

        资源名称

        :param metric_name: The metric_name of this ShowStatusAppResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def app_list(self):
        r"""Gets the app_list of this ShowStatusAppResponse.

        应用列表

        :return: The app_list of this ShowStatusAppResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusAppItem`]
        """
        return self._app_list

    @app_list.setter
    def app_list(self, app_list):
        r"""Sets the app_list of this ShowStatusAppResponse.

        应用列表

        :param app_list: The app_list of this ShowStatusAppResponse.
        :type app_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusAppItem`]
        """
        self._app_list = app_list

    @property
    def total_access_count(self):
        r"""Gets the total_access_count of this ShowStatusAppResponse.

        总访问次数

        :return: The total_access_count of this ShowStatusAppResponse.
        :rtype: int
        """
        return self._total_access_count

    @total_access_count.setter
    def total_access_count(self, total_access_count):
        r"""Sets the total_access_count of this ShowStatusAppResponse.

        总访问次数

        :param total_access_count: The total_access_count of this ShowStatusAppResponse.
        :type total_access_count: int
        """
        self._total_access_count = total_access_count

    @property
    def success_access_count(self):
        r"""Gets the success_access_count of this ShowStatusAppResponse.

        成功访问次数

        :return: The success_access_count of this ShowStatusAppResponse.
        :rtype: int
        """
        return self._success_access_count

    @success_access_count.setter
    def success_access_count(self, success_access_count):
        r"""Sets the success_access_count of this ShowStatusAppResponse.

        成功访问次数

        :param success_access_count: The success_access_count of this ShowStatusAppResponse.
        :type success_access_count: int
        """
        self._success_access_count = success_access_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatusAppResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowStatusAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
