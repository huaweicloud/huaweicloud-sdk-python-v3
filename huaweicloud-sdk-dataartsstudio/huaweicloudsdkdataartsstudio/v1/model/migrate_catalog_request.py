# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateCatalogRequest:

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
        'dlm_type': 'str',
        'catalog_id': 'str',
        'body': 'CatalogMoveParaDTO'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'catalog_id': 'catalog_id',
        'body': 'body'
    }

    def __init__(self, workspace=None, dlm_type=None, catalog_id=None, body=None):
        r"""MigrateCatalogRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param catalog_id: 目录编号。
        :type catalog_id: str
        :param body: Body of the MigrateCatalogRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.CatalogMoveParaDTO`
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._catalog_id = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        self.catalog_id = catalog_id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        r"""Gets the workspace of this MigrateCatalogRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this MigrateCatalogRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this MigrateCatalogRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this MigrateCatalogRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        r"""Gets the dlm_type of this MigrateCatalogRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this MigrateCatalogRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        r"""Sets the dlm_type of this MigrateCatalogRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this MigrateCatalogRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def catalog_id(self):
        r"""Gets the catalog_id of this MigrateCatalogRequest.

        目录编号。

        :return: The catalog_id of this MigrateCatalogRequest.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        r"""Sets the catalog_id of this MigrateCatalogRequest.

        目录编号。

        :param catalog_id: The catalog_id of this MigrateCatalogRequest.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def body(self):
        r"""Gets the body of this MigrateCatalogRequest.

        :return: The body of this MigrateCatalogRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CatalogMoveParaDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this MigrateCatalogRequest.

        :param body: The body of this MigrateCatalogRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.CatalogMoveParaDTO`
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
        if not isinstance(other, MigrateCatalogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
