# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AcceptSecurityApplicationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'id': 'str',
        'body': 'ReasonDTO'
    }

    attribute_map = {
        'workspace': 'workspace',
        'id': 'id',
        'body': 'body'
    }

    def __init__(self, workspace=None, id=None, body=None):
        r"""AcceptSecurityApplicationRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param id: 工单id
        :type id: str
        :param body: Body of the AcceptSecurityApplicationRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ReasonDTO`
        """
        
        

        self._workspace = None
        self._id = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.id = id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        r"""Gets the workspace of this AcceptSecurityApplicationRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this AcceptSecurityApplicationRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this AcceptSecurityApplicationRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this AcceptSecurityApplicationRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def id(self):
        r"""Gets the id of this AcceptSecurityApplicationRequest.

        工单id

        :return: The id of this AcceptSecurityApplicationRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AcceptSecurityApplicationRequest.

        工单id

        :param id: The id of this AcceptSecurityApplicationRequest.
        :type id: str
        """
        self._id = id

    @property
    def body(self):
        r"""Gets the body of this AcceptSecurityApplicationRequest.

        :return: The body of this AcceptSecurityApplicationRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ReasonDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AcceptSecurityApplicationRequest.

        :param body: The body of this AcceptSecurityApplicationRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ReasonDTO`
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
        if not isinstance(other, AcceptSecurityApplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
