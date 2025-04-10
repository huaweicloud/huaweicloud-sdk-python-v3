# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddTagToAssetRequest:

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
        'term_guid': 'str',
        'body': 'CatalogInfo'
    }

    attribute_map = {
        'workspace': 'workspace',
        'term_guid': 'term_guid',
        'body': 'body'
    }

    def __init__(self, workspace=None, term_guid=None, body=None):
        r"""AddTagToAssetRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param term_guid: guid
        :type term_guid: str
        :param body: Body of the AddTagToAssetRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.CatalogInfo`
        """
        
        

        self._workspace = None
        self._term_guid = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.term_guid = term_guid
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        r"""Gets the workspace of this AddTagToAssetRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this AddTagToAssetRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this AddTagToAssetRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this AddTagToAssetRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def term_guid(self):
        r"""Gets the term_guid of this AddTagToAssetRequest.

        guid

        :return: The term_guid of this AddTagToAssetRequest.
        :rtype: str
        """
        return self._term_guid

    @term_guid.setter
    def term_guid(self, term_guid):
        r"""Sets the term_guid of this AddTagToAssetRequest.

        guid

        :param term_guid: The term_guid of this AddTagToAssetRequest.
        :type term_guid: str
        """
        self._term_guid = term_guid

    @property
    def body(self):
        r"""Gets the body of this AddTagToAssetRequest.

        :return: The body of this AddTagToAssetRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CatalogInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AddTagToAssetRequest.

        :param body: The body of this AddTagToAssetRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.CatalogInfo`
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
        if not isinstance(other, AddTagToAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
