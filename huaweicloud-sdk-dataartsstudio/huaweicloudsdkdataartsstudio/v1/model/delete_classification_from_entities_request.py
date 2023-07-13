# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteClassificationFromEntitiesRequest:

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
        'guid': 'str',
        'body': 'OpenClassification'
    }

    attribute_map = {
        'workspace': 'workspace',
        'guid': 'guid',
        'body': 'body'
    }

    def __init__(self, workspace=None, guid=None, body=None):
        """DeleteClassificationFromEntitiesRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param guid: 资产标识guid
        :type guid: str
        :param body: Body of the DeleteClassificationFromEntitiesRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.OpenClassification`
        """
        
        

        self._workspace = None
        self._guid = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.guid = guid
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this DeleteClassificationFromEntitiesRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this DeleteClassificationFromEntitiesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this DeleteClassificationFromEntitiesRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this DeleteClassificationFromEntitiesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def guid(self):
        """Gets the guid of this DeleteClassificationFromEntitiesRequest.

        资产标识guid

        :return: The guid of this DeleteClassificationFromEntitiesRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this DeleteClassificationFromEntitiesRequest.

        资产标识guid

        :param guid: The guid of this DeleteClassificationFromEntitiesRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def body(self):
        """Gets the body of this DeleteClassificationFromEntitiesRequest.

        :return: The body of this DeleteClassificationFromEntitiesRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.OpenClassification`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteClassificationFromEntitiesRequest.

        :param body: The body of this DeleteClassificationFromEntitiesRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.OpenClassification`
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
        if not isinstance(other, DeleteClassificationFromEntitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
