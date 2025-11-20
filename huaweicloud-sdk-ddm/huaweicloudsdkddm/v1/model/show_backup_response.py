# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupResponse(SdkResponse):

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
        'name': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'related_data_nodes': 'list[RelatedDn]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'related_data_nodes': 'related_data_nodes'
    }

    def __init__(self, id=None, name=None, instance_id=None, instance_name=None, related_data_nodes=None):
        r"""ShowBackupResponse

        The model defined in huaweicloud sdk

        :param id: 备份id。
        :type id: str
        :param name: 备份名称。
        :type name: str
        :param instance_id: 实例id。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param related_data_nodes: 关联DN。
        :type related_data_nodes: list[:class:`huaweicloudsdkddm.v1.RelatedDn`]
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._instance_id = None
        self._instance_name = None
        self._related_data_nodes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if related_data_nodes is not None:
            self.related_data_nodes = related_data_nodes

    @property
    def id(self):
        r"""Gets the id of this ShowBackupResponse.

        备份id。

        :return: The id of this ShowBackupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowBackupResponse.

        备份id。

        :param id: The id of this ShowBackupResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowBackupResponse.

        备份名称。

        :return: The name of this ShowBackupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBackupResponse.

        备份名称。

        :param name: The name of this ShowBackupResponse.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowBackupResponse.

        实例id。

        :return: The instance_id of this ShowBackupResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowBackupResponse.

        实例id。

        :param instance_id: The instance_id of this ShowBackupResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowBackupResponse.

        实例名称。

        :return: The instance_name of this ShowBackupResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowBackupResponse.

        实例名称。

        :param instance_name: The instance_name of this ShowBackupResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def related_data_nodes(self):
        r"""Gets the related_data_nodes of this ShowBackupResponse.

        关联DN。

        :return: The related_data_nodes of this ShowBackupResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.RelatedDn`]
        """
        return self._related_data_nodes

    @related_data_nodes.setter
    def related_data_nodes(self, related_data_nodes):
        r"""Sets the related_data_nodes of this ShowBackupResponse.

        关联DN。

        :param related_data_nodes: The related_data_nodes of this ShowBackupResponse.
        :type related_data_nodes: list[:class:`huaweicloudsdkddm.v1.RelatedDn`]
        """
        self._related_data_nodes = related_data_nodes

    def to_dict(self):
        import warnings
        warnings.warn("ShowBackupResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowBackupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
