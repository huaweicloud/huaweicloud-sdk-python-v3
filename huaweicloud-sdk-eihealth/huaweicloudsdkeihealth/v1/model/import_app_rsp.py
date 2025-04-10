# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportAppRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_app_id': 'str',
        'destination_app_id': 'str',
        'destination_app_name': 'str',
        'version': 'str',
        'message': 'str',
        'status': 'str'
    }

    attribute_map = {
        'source_app_id': 'source_app_id',
        'destination_app_id': 'destination_app_id',
        'destination_app_name': 'destination_app_name',
        'version': 'version',
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, source_app_id=None, destination_app_id=None, destination_app_name=None, version=None, message=None, status=None):
        r"""ImportAppRsp

        The model defined in huaweicloud sdk

        :param source_app_id: 源应用id
        :type source_app_id: str
        :param destination_app_id: 目标应用id
        :type destination_app_id: str
        :param destination_app_name: 目标应用名称
        :type destination_app_name: str
        :param version: 应用版本
        :type version: str
        :param message: 导入结果信息，仅在导入失败时会返回
        :type message: str
        :param status: 导入结果状态
        :type status: str
        """
        
        

        self._source_app_id = None
        self._destination_app_id = None
        self._destination_app_name = None
        self._version = None
        self._message = None
        self._status = None
        self.discriminator = None

        if source_app_id is not None:
            self.source_app_id = source_app_id
        if destination_app_id is not None:
            self.destination_app_id = destination_app_id
        if destination_app_name is not None:
            self.destination_app_name = destination_app_name
        if version is not None:
            self.version = version
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def source_app_id(self):
        r"""Gets the source_app_id of this ImportAppRsp.

        源应用id

        :return: The source_app_id of this ImportAppRsp.
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        r"""Sets the source_app_id of this ImportAppRsp.

        源应用id

        :param source_app_id: The source_app_id of this ImportAppRsp.
        :type source_app_id: str
        """
        self._source_app_id = source_app_id

    @property
    def destination_app_id(self):
        r"""Gets the destination_app_id of this ImportAppRsp.

        目标应用id

        :return: The destination_app_id of this ImportAppRsp.
        :rtype: str
        """
        return self._destination_app_id

    @destination_app_id.setter
    def destination_app_id(self, destination_app_id):
        r"""Sets the destination_app_id of this ImportAppRsp.

        目标应用id

        :param destination_app_id: The destination_app_id of this ImportAppRsp.
        :type destination_app_id: str
        """
        self._destination_app_id = destination_app_id

    @property
    def destination_app_name(self):
        r"""Gets the destination_app_name of this ImportAppRsp.

        目标应用名称

        :return: The destination_app_name of this ImportAppRsp.
        :rtype: str
        """
        return self._destination_app_name

    @destination_app_name.setter
    def destination_app_name(self, destination_app_name):
        r"""Sets the destination_app_name of this ImportAppRsp.

        目标应用名称

        :param destination_app_name: The destination_app_name of this ImportAppRsp.
        :type destination_app_name: str
        """
        self._destination_app_name = destination_app_name

    @property
    def version(self):
        r"""Gets the version of this ImportAppRsp.

        应用版本

        :return: The version of this ImportAppRsp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ImportAppRsp.

        应用版本

        :param version: The version of this ImportAppRsp.
        :type version: str
        """
        self._version = version

    @property
    def message(self):
        r"""Gets the message of this ImportAppRsp.

        导入结果信息，仅在导入失败时会返回

        :return: The message of this ImportAppRsp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ImportAppRsp.

        导入结果信息，仅在导入失败时会返回

        :param message: The message of this ImportAppRsp.
        :type message: str
        """
        self._message = message

    @property
    def status(self):
        r"""Gets the status of this ImportAppRsp.

        导入结果状态

        :return: The status of this ImportAppRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ImportAppRsp.

        导入结果状态

        :param status: The status of this ImportAppRsp.
        :type status: str
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
        if not isinstance(other, ImportAppRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
