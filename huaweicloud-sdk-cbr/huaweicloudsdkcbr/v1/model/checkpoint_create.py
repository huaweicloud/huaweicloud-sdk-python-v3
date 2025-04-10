# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointCreate:

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
        'project_id': 'str',
        'status': 'str',
        'vault': 'CheckpointPlanCreate',
        'extra_info': 'CheckpointExtraInfoResp'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'project_id': 'project_id',
        'status': 'status',
        'vault': 'vault',
        'extra_info': 'extra_info'
    }

    def __init__(self, created_at=None, id=None, project_id=None, status=None, vault=None, extra_info=None):
        r"""CheckpointCreate

        The model defined in huaweicloud sdk

        :param created_at: 创建时间，例如:\&quot;2020-02-05T10:38:34.209782\&quot;
        :type created_at: str
        :param id: 还原点ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param status: 状态:available,deleting,protecting,deleted,error-deleting,error
        :type status: str
        :param vault: 
        :type vault: :class:`huaweicloudsdkcbr.v1.CheckpointPlanCreate`
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkcbr.v1.CheckpointExtraInfoResp`
        """
        
        

        self._created_at = None
        self._id = None
        self._project_id = None
        self._status = None
        self._vault = None
        self._extra_info = None
        self.discriminator = None

        self.created_at = created_at
        self.id = id
        self.project_id = project_id
        self.status = status
        if vault is not None:
            self.vault = vault
        if extra_info is not None:
            self.extra_info = extra_info

    @property
    def created_at(self):
        r"""Gets the created_at of this CheckpointCreate.

        创建时间，例如:\"2020-02-05T10:38:34.209782\"

        :return: The created_at of this CheckpointCreate.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CheckpointCreate.

        创建时间，例如:\"2020-02-05T10:38:34.209782\"

        :param created_at: The created_at of this CheckpointCreate.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this CheckpointCreate.

        还原点ID

        :return: The id of this CheckpointCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CheckpointCreate.

        还原点ID

        :param id: The id of this CheckpointCreate.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this CheckpointCreate.

        项目ID

        :return: The project_id of this CheckpointCreate.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CheckpointCreate.

        项目ID

        :param project_id: The project_id of this CheckpointCreate.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this CheckpointCreate.

        状态:available,deleting,protecting,deleted,error-deleting,error

        :return: The status of this CheckpointCreate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CheckpointCreate.

        状态:available,deleting,protecting,deleted,error-deleting,error

        :param status: The status of this CheckpointCreate.
        :type status: str
        """
        self._status = status

    @property
    def vault(self):
        r"""Gets the vault of this CheckpointCreate.

        :return: The vault of this CheckpointCreate.
        :rtype: :class:`huaweicloudsdkcbr.v1.CheckpointPlanCreate`
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        r"""Sets the vault of this CheckpointCreate.

        :param vault: The vault of this CheckpointCreate.
        :type vault: :class:`huaweicloudsdkcbr.v1.CheckpointPlanCreate`
        """
        self._vault = vault

    @property
    def extra_info(self):
        r"""Gets the extra_info of this CheckpointCreate.

        :return: The extra_info of this CheckpointCreate.
        :rtype: :class:`huaweicloudsdkcbr.v1.CheckpointExtraInfoResp`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this CheckpointCreate.

        :param extra_info: The extra_info of this CheckpointCreate.
        :type extra_info: :class:`huaweicloudsdkcbr.v1.CheckpointExtraInfoResp`
        """
        self._extra_info = extra_info

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
        if not isinstance(other, CheckpointCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
