# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'release_dev': 'str',
        'result_code': 'str',
        'test_result_uri': 'str',
        'status_code': 'str',
        'version_uri': 'str'
    }

    attribute_map = {
        'description': 'description',
        'release_dev': 'release_dev',
        'result_code': 'result_code',
        'test_result_uri': 'test_result_uri',
        'status_code': 'status_code',
        'version_uri': 'version_uri'
    }

    def __init__(self, description=None, release_dev=None, result_code=None, test_result_uri=None, status_code=None, version_uri=None):
        r"""ExecuteTaskInfo

        The model defined in huaweicloud sdk

        :param description: 描述
        :type description: str
        :param release_dev: 发布版本号
        :type release_dev: str
        :param result_code: 结果Code
        :type result_code: str
        :param test_result_uri: 任务执行结果Uri
        :type test_result_uri: str
        :param status_code: 状态Code
        :type status_code: str
        :param version_uri: 分支/迭代uri
        :type version_uri: str
        """
        
        

        self._description = None
        self._release_dev = None
        self._result_code = None
        self._test_result_uri = None
        self._status_code = None
        self._version_uri = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if release_dev is not None:
            self.release_dev = release_dev
        if result_code is not None:
            self.result_code = result_code
        if test_result_uri is not None:
            self.test_result_uri = test_result_uri
        if status_code is not None:
            self.status_code = status_code
        if version_uri is not None:
            self.version_uri = version_uri

    @property
    def description(self):
        r"""Gets the description of this ExecuteTaskInfo.

        描述

        :return: The description of this ExecuteTaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExecuteTaskInfo.

        描述

        :param description: The description of this ExecuteTaskInfo.
        :type description: str
        """
        self._description = description

    @property
    def release_dev(self):
        r"""Gets the release_dev of this ExecuteTaskInfo.

        发布版本号

        :return: The release_dev of this ExecuteTaskInfo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this ExecuteTaskInfo.

        发布版本号

        :param release_dev: The release_dev of this ExecuteTaskInfo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def result_code(self):
        r"""Gets the result_code of this ExecuteTaskInfo.

        结果Code

        :return: The result_code of this ExecuteTaskInfo.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this ExecuteTaskInfo.

        结果Code

        :param result_code: The result_code of this ExecuteTaskInfo.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def test_result_uri(self):
        r"""Gets the test_result_uri of this ExecuteTaskInfo.

        任务执行结果Uri

        :return: The test_result_uri of this ExecuteTaskInfo.
        :rtype: str
        """
        return self._test_result_uri

    @test_result_uri.setter
    def test_result_uri(self, test_result_uri):
        r"""Sets the test_result_uri of this ExecuteTaskInfo.

        任务执行结果Uri

        :param test_result_uri: The test_result_uri of this ExecuteTaskInfo.
        :type test_result_uri: str
        """
        self._test_result_uri = test_result_uri

    @property
    def status_code(self):
        r"""Gets the status_code of this ExecuteTaskInfo.

        状态Code

        :return: The status_code of this ExecuteTaskInfo.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this ExecuteTaskInfo.

        状态Code

        :param status_code: The status_code of this ExecuteTaskInfo.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def version_uri(self):
        r"""Gets the version_uri of this ExecuteTaskInfo.

        分支/迭代uri

        :return: The version_uri of this ExecuteTaskInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this ExecuteTaskInfo.

        分支/迭代uri

        :param version_uri: The version_uri of this ExecuteTaskInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

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
        if not isinstance(other, ExecuteTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
