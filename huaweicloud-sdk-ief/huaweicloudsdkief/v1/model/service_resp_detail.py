# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceRespDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'id': 'str',
        'meta_data': 'SvcMetadata',
        'project_id': 'str',
        'spec': 'SvcSpec',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'meta_data': 'meta_data',
        'project_id': 'project_id',
        'spec': 'spec',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, id=None, meta_data=None, project_id=None, spec=None, updated_at=None):
        r"""ServiceRespDetail

        The model defined in huaweicloud sdk

        :param created_at: 创建时间
        :type created_at: str
        :param id: 服务ID
        :type id: str
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkief.v1.SvcMetadata`
        :param project_id: 租户ID
        :type project_id: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkief.v1.SvcSpec`
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._created_at = None
        self._id = None
        self._meta_data = None
        self._project_id = None
        self._spec = None
        self._updated_at = None
        self.discriminator = None

        self.created_at = created_at
        self.id = id
        self.meta_data = meta_data
        self.project_id = project_id
        self.spec = spec
        self.updated_at = updated_at

    @property
    def created_at(self):
        r"""Gets the created_at of this ServiceRespDetail.

        创建时间

        :return: The created_at of this ServiceRespDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ServiceRespDetail.

        创建时间

        :param created_at: The created_at of this ServiceRespDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this ServiceRespDetail.

        服务ID

        :return: The id of this ServiceRespDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServiceRespDetail.

        服务ID

        :param id: The id of this ServiceRespDetail.
        :type id: str
        """
        self._id = id

    @property
    def meta_data(self):
        r"""Gets the meta_data of this ServiceRespDetail.

        :return: The meta_data of this ServiceRespDetail.
        :rtype: :class:`huaweicloudsdkief.v1.SvcMetadata`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this ServiceRespDetail.

        :param meta_data: The meta_data of this ServiceRespDetail.
        :type meta_data: :class:`huaweicloudsdkief.v1.SvcMetadata`
        """
        self._meta_data = meta_data

    @property
    def project_id(self):
        r"""Gets the project_id of this ServiceRespDetail.

        租户ID

        :return: The project_id of this ServiceRespDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ServiceRespDetail.

        租户ID

        :param project_id: The project_id of this ServiceRespDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def spec(self):
        r"""Gets the spec of this ServiceRespDetail.

        :return: The spec of this ServiceRespDetail.
        :rtype: :class:`huaweicloudsdkief.v1.SvcSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ServiceRespDetail.

        :param spec: The spec of this ServiceRespDetail.
        :type spec: :class:`huaweicloudsdkief.v1.SvcSpec`
        """
        self._spec = spec

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ServiceRespDetail.

        更新时间

        :return: The updated_at of this ServiceRespDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ServiceRespDetail.

        更新时间

        :param updated_at: The updated_at of this ServiceRespDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ServiceRespDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
