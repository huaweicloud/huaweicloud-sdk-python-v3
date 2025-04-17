# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTestcasePlansRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'branch_uri': 'str',
        'body': 'TestcasePlanQueryParam'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'branch_uri': 'branch_uri',
        'body': 'body'
    }

    def __init__(self, project_uuid=None, branch_uri=None, body=None):
        r"""ListTestcasePlansRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param branch_uri: 版本URI
        :type branch_uri: str
        :param body: Body of the ListTestcasePlansRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestcasePlanQueryParam`
        """
        
        

        self._project_uuid = None
        self._branch_uri = None
        self._body = None
        self.discriminator = None

        self.project_uuid = project_uuid
        self.branch_uri = branch_uri
        if body is not None:
            self.body = body

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ListTestcasePlansRequest.

        项目id

        :return: The project_uuid of this ListTestcasePlansRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ListTestcasePlansRequest.

        项目id

        :param project_uuid: The project_uuid of this ListTestcasePlansRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def branch_uri(self):
        r"""Gets the branch_uri of this ListTestcasePlansRequest.

        版本URI

        :return: The branch_uri of this ListTestcasePlansRequest.
        :rtype: str
        """
        return self._branch_uri

    @branch_uri.setter
    def branch_uri(self, branch_uri):
        r"""Sets the branch_uri of this ListTestcasePlansRequest.

        版本URI

        :param branch_uri: The branch_uri of this ListTestcasePlansRequest.
        :type branch_uri: str
        """
        self._branch_uri = branch_uri

    @property
    def body(self):
        r"""Gets the body of this ListTestcasePlansRequest.

        :return: The body of this ListTestcasePlansRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestcasePlanQueryParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListTestcasePlansRequest.

        :param body: The body of this ListTestcasePlansRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestcasePlanQueryParam`
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
        if not isinstance(other, ListTestcasePlansRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
