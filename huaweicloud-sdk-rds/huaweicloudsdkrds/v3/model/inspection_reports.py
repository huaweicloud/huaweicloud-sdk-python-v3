# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InspectionReports:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'check_time': 'str',
        'expiration_time': 'str',
        'target_version': 'str',
        'result': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'id': 'id',
        'check_time': 'check_time',
        'expiration_time': 'expiration_time',
        'target_version': 'target_version',
        'result': 'result',
        'detail': 'detail'
    }

    def __init__(self, id=None, check_time=None, expiration_time=None, target_version=None, result=None, detail=None):
        r"""InspectionReports

        The model defined in huaweicloud sdk

        :param id: 检查报告ID。
        :type id: str
        :param check_time: 检查时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type check_time: str
        :param expiration_time: 到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type expiration_time: str
        :param target_version: 目标版本。
        :type target_version: str
        :param result: 检查结果。 success，表示成功。 failed，表示失败。 running， 表示检查中。
        :type result: str
        :param detail: 检查报告详情。
        :type detail: str
        """
        
        

        self._id = None
        self._check_time = None
        self._expiration_time = None
        self._target_version = None
        self._result = None
        self._detail = None
        self.discriminator = None

        self.id = id
        self.check_time = check_time
        self.expiration_time = expiration_time
        self.target_version = target_version
        self.result = result
        self.detail = detail

    @property
    def id(self):
        r"""Gets the id of this InspectionReports.

        检查报告ID。

        :return: The id of this InspectionReports.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InspectionReports.

        检查报告ID。

        :param id: The id of this InspectionReports.
        :type id: str
        """
        self._id = id

    @property
    def check_time(self):
        r"""Gets the check_time of this InspectionReports.

        检查时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The check_time of this InspectionReports.
        :rtype: str
        """
        return self._check_time

    @check_time.setter
    def check_time(self, check_time):
        r"""Sets the check_time of this InspectionReports.

        检查时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param check_time: The check_time of this InspectionReports.
        :type check_time: str
        """
        self._check_time = check_time

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this InspectionReports.

        到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The expiration_time of this InspectionReports.
        :rtype: str
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this InspectionReports.

        到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param expiration_time: The expiration_time of this InspectionReports.
        :type expiration_time: str
        """
        self._expiration_time = expiration_time

    @property
    def target_version(self):
        r"""Gets the target_version of this InspectionReports.

        目标版本。

        :return: The target_version of this InspectionReports.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this InspectionReports.

        目标版本。

        :param target_version: The target_version of this InspectionReports.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def result(self):
        r"""Gets the result of this InspectionReports.

        检查结果。 success，表示成功。 failed，表示失败。 running， 表示检查中。

        :return: The result of this InspectionReports.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this InspectionReports.

        检查结果。 success，表示成功。 failed，表示失败。 running， 表示检查中。

        :param result: The result of this InspectionReports.
        :type result: str
        """
        self._result = result

    @property
    def detail(self):
        r"""Gets the detail of this InspectionReports.

        检查报告详情。

        :return: The detail of this InspectionReports.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this InspectionReports.

        检查报告详情。

        :param detail: The detail of this InspectionReports.
        :type detail: str
        """
        self._detail = detail

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
        if not isinstance(other, InspectionReports):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
