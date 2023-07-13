# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTemplateRequest:

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
        'workspace': 'str',
        'body': 'TemplateRO'
    }

    attribute_map = {
        'id': 'id',
        'workspace': 'workspace',
        'body': 'body'
    }

    def __init__(self, id=None, workspace=None, body=None):
        """UpdateTemplateRequest

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param workspace: workspace 信息
        :type workspace: str
        :param body: Body of the UpdateTemplateRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.TemplateRO`
        """
        
        

        self._id = None
        self._workspace = None
        self._body = None
        self.discriminator = None

        self.id = id
        self.workspace = workspace
        if body is not None:
            self.body = body

    @property
    def id(self):
        """Gets the id of this UpdateTemplateRequest.

        id

        :return: The id of this UpdateTemplateRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateTemplateRequest.

        id

        :param id: The id of this UpdateTemplateRequest.
        :type id: str
        """
        self._id = id

    @property
    def workspace(self):
        """Gets the workspace of this UpdateTemplateRequest.

        workspace 信息

        :return: The workspace of this UpdateTemplateRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this UpdateTemplateRequest.

        workspace 信息

        :param workspace: The workspace of this UpdateTemplateRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def body(self):
        """Gets the body of this UpdateTemplateRequest.

        :return: The body of this UpdateTemplateRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.TemplateRO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateTemplateRequest.

        :param body: The body of this UpdateTemplateRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.TemplateRO`
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
        if not isinstance(other, UpdateTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
