# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreBackupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'eihealth_project_id': 'str',
        'body': 'RestoreBackupReq'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'eihealth_project_id': 'eihealth_project_id',
        'body': 'body'
    }

    def __init__(self, backup_id=None, eihealth_project_id=None, body=None):
        r"""RestoreBackupRequest

        The model defined in huaweicloud sdk

        :param backup_id: 归档ID
        :type backup_id: str
        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param body: Body of the RestoreBackupRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.RestoreBackupReq`
        """
        
        

        self._backup_id = None
        self._eihealth_project_id = None
        self._body = None
        self.discriminator = None

        self.backup_id = backup_id
        self.eihealth_project_id = eihealth_project_id
        if body is not None:
            self.body = body

    @property
    def backup_id(self):
        r"""Gets the backup_id of this RestoreBackupRequest.

        归档ID

        :return: The backup_id of this RestoreBackupRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RestoreBackupRequest.

        归档ID

        :param backup_id: The backup_id of this RestoreBackupRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this RestoreBackupRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this RestoreBackupRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this RestoreBackupRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this RestoreBackupRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def body(self):
        r"""Gets the body of this RestoreBackupRequest.

        :return: The body of this RestoreBackupRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.RestoreBackupReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RestoreBackupRequest.

        :param body: The body of this RestoreBackupRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.RestoreBackupReq`
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
        if not isinstance(other, RestoreBackupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
