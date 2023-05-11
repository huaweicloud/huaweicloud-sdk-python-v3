# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveDataExportReq:

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
        'format': 'str',
        'apis': 'list[str]',
        'status': 'int'
    }

    attribute_map = {
        'app_id': 'app_id',
        'format': 'format',
        'apis': 'apis',
        'status': 'status'
    }

    def __init__(self, app_id=None, format=None, apis=None, status=None):
        """LiveDataExportReq

        The model defined in huaweicloud sdk

        :param app_id: API所属的应用ID
        :type app_id: str
        :param format: 导出的API定义的格式
        :type format: str
        :param apis: 导出的自定义后端API ID列表
        :type apis: list[str]
        :param status: 导出的后端API状态： - 1：待开发 - 3：开发中 - 4：已部署
        :type status: int
        """
        
        

        self._app_id = None
        self._format = None
        self._apis = None
        self._status = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if format is not None:
            self.format = format
        if apis is not None:
            self.apis = apis
        if status is not None:
            self.status = status

    @property
    def app_id(self):
        """Gets the app_id of this LiveDataExportReq.

        API所属的应用ID

        :return: The app_id of this LiveDataExportReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this LiveDataExportReq.

        API所属的应用ID

        :param app_id: The app_id of this LiveDataExportReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def format(self):
        """Gets the format of this LiveDataExportReq.

        导出的API定义的格式

        :return: The format of this LiveDataExportReq.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this LiveDataExportReq.

        导出的API定义的格式

        :param format: The format of this LiveDataExportReq.
        :type format: str
        """
        self._format = format

    @property
    def apis(self):
        """Gets the apis of this LiveDataExportReq.

        导出的自定义后端API ID列表

        :return: The apis of this LiveDataExportReq.
        :rtype: list[str]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        """Sets the apis of this LiveDataExportReq.

        导出的自定义后端API ID列表

        :param apis: The apis of this LiveDataExportReq.
        :type apis: list[str]
        """
        self._apis = apis

    @property
    def status(self):
        """Gets the status of this LiveDataExportReq.

        导出的后端API状态： - 1：待开发 - 3：开发中 - 4：已部署

        :return: The status of this LiveDataExportReq.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LiveDataExportReq.

        导出的后端API状态： - 1：待开发 - 3：开发中 - 4：已部署

        :param status: The status of this LiveDataExportReq.
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
        if not isinstance(other, LiveDataExportReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
