# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoJobResponseHostingResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'str',
        'obs': 'object',
        'status': 'str',
        'result_json_overdue_at': 'str'
    }

    attribute_map = {
        'data': 'data',
        'obs': 'obs',
        'status': 'status',
        'result_json_overdue_at': 'result_json_overdue_at'
    }

    def __init__(self, data=None, obs=None, status=None, result_json_overdue_at=None):
        """VideoJobResponseHostingResult

        The model defined in huaweicloud sdk

        :param data: 结果文件result.json的具体内容。
        :type data: str
        :param obs: 结果文件所在的OBS桶和result.json文件路径
        :type obs: object
        :param status: result.json文件的状态： - NOT_GENERATED：文件未生成 - AVAILABLE：文件可获取 - EXCEED_IN_SIZE：文件超过最大规格 - OVERDUE：文件过期 - DELETED_MISTAKENLY：文件误删除
        :type status: str
        :param result_json_overdue_at: result.json文件的过期日期，文件默认保存48小时。
        :type result_json_overdue_at: str
        """
        
        

        self._data = None
        self._obs = None
        self._status = None
        self._result_json_overdue_at = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if obs is not None:
            self.obs = obs
        if status is not None:
            self.status = status
        if result_json_overdue_at is not None:
            self.result_json_overdue_at = result_json_overdue_at

    @property
    def data(self):
        """Gets the data of this VideoJobResponseHostingResult.

        结果文件result.json的具体内容。

        :return: The data of this VideoJobResponseHostingResult.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VideoJobResponseHostingResult.

        结果文件result.json的具体内容。

        :param data: The data of this VideoJobResponseHostingResult.
        :type data: str
        """
        self._data = data

    @property
    def obs(self):
        """Gets the obs of this VideoJobResponseHostingResult.

        结果文件所在的OBS桶和result.json文件路径

        :return: The obs of this VideoJobResponseHostingResult.
        :rtype: object
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this VideoJobResponseHostingResult.

        结果文件所在的OBS桶和result.json文件路径

        :param obs: The obs of this VideoJobResponseHostingResult.
        :type obs: object
        """
        self._obs = obs

    @property
    def status(self):
        """Gets the status of this VideoJobResponseHostingResult.

        result.json文件的状态： - NOT_GENERATED：文件未生成 - AVAILABLE：文件可获取 - EXCEED_IN_SIZE：文件超过最大规格 - OVERDUE：文件过期 - DELETED_MISTAKENLY：文件误删除

        :return: The status of this VideoJobResponseHostingResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VideoJobResponseHostingResult.

        result.json文件的状态： - NOT_GENERATED：文件未生成 - AVAILABLE：文件可获取 - EXCEED_IN_SIZE：文件超过最大规格 - OVERDUE：文件过期 - DELETED_MISTAKENLY：文件误删除

        :param status: The status of this VideoJobResponseHostingResult.
        :type status: str
        """
        self._status = status

    @property
    def result_json_overdue_at(self):
        """Gets the result_json_overdue_at of this VideoJobResponseHostingResult.

        result.json文件的过期日期，文件默认保存48小时。

        :return: The result_json_overdue_at of this VideoJobResponseHostingResult.
        :rtype: str
        """
        return self._result_json_overdue_at

    @result_json_overdue_at.setter
    def result_json_overdue_at(self, result_json_overdue_at):
        """Sets the result_json_overdue_at of this VideoJobResponseHostingResult.

        result.json文件的过期日期，文件默认保存48小时。

        :param result_json_overdue_at: The result_json_overdue_at of this VideoJobResponseHostingResult.
        :type result_json_overdue_at: str
        """
        self._result_json_overdue_at = result_json_overdue_at

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
        if not isinstance(other, VideoJobResponseHostingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
