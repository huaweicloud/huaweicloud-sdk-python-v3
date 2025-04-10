# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTestCaseAndScriptRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'tmss_case_uri': 'str',
        'turn_on_awmapping': 'bool',
        'body': 'CreateTestCaseReq'
    }

    attribute_map = {
        'project_id': 'project_id',
        'tmss_case_uri': 'tmss_case_uri',
        'turn_on_awmapping': 'turn_on_awmapping',
        'body': 'body'
    }

    def __init__(self, project_id=None, tmss_case_uri=None, turn_on_awmapping=None, body=None):
        r"""UpdateTestCaseAndScriptRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param tmss_case_uri: TMSS用例uri
        :type tmss_case_uri: str
        :param turn_on_awmapping: 新组合AW开关
        :type turn_on_awmapping: bool
        :param body: Body of the UpdateTestCaseAndScriptRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.CreateTestCaseReq`
        """
        
        

        self._project_id = None
        self._tmss_case_uri = None
        self._turn_on_awmapping = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.tmss_case_uri = tmss_case_uri
        if turn_on_awmapping is not None:
            self.turn_on_awmapping = turn_on_awmapping
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateTestCaseAndScriptRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this UpdateTestCaseAndScriptRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateTestCaseAndScriptRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this UpdateTestCaseAndScriptRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tmss_case_uri(self):
        r"""Gets the tmss_case_uri of this UpdateTestCaseAndScriptRequest.

        TMSS用例uri

        :return: The tmss_case_uri of this UpdateTestCaseAndScriptRequest.
        :rtype: str
        """
        return self._tmss_case_uri

    @tmss_case_uri.setter
    def tmss_case_uri(self, tmss_case_uri):
        r"""Sets the tmss_case_uri of this UpdateTestCaseAndScriptRequest.

        TMSS用例uri

        :param tmss_case_uri: The tmss_case_uri of this UpdateTestCaseAndScriptRequest.
        :type tmss_case_uri: str
        """
        self._tmss_case_uri = tmss_case_uri

    @property
    def turn_on_awmapping(self):
        r"""Gets the turn_on_awmapping of this UpdateTestCaseAndScriptRequest.

        新组合AW开关

        :return: The turn_on_awmapping of this UpdateTestCaseAndScriptRequest.
        :rtype: bool
        """
        return self._turn_on_awmapping

    @turn_on_awmapping.setter
    def turn_on_awmapping(self, turn_on_awmapping):
        r"""Sets the turn_on_awmapping of this UpdateTestCaseAndScriptRequest.

        新组合AW开关

        :param turn_on_awmapping: The turn_on_awmapping of this UpdateTestCaseAndScriptRequest.
        :type turn_on_awmapping: bool
        """
        self._turn_on_awmapping = turn_on_awmapping

    @property
    def body(self):
        r"""Gets the body of this UpdateTestCaseAndScriptRequest.

        :return: The body of this UpdateTestCaseAndScriptRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateTestCaseReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTestCaseAndScriptRequest.

        :param body: The body of this UpdateTestCaseAndScriptRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.CreateTestCaseReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateTestCaseAndScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
