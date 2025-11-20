# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadSchemaMetadataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compressed_databases_info': 'str',
        'dn_instance': 'list[DNInstance]',
        'instance_id': 'str',
        'project_id': 'str',
        'iam_account': 'IamAccount'
    }

    attribute_map = {
        'compressed_databases_info': 'compressed_databases_info',
        'dn_instance': 'dn_instance',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'iam_account': 'iam_account'
    }

    def __init__(self, compressed_databases_info=None, dn_instance=None, instance_id=None, project_id=None, iam_account=None):
        r"""LoadSchemaMetadataReq

        The model defined in huaweicloud sdk

        :param compressed_databases_info: 逻辑库信息。
        :type compressed_databases_info: str
        :param dn_instance: 关联的后端DN信息。
        :type dn_instance: list[:class:`huaweicloudsdkddm.v1.DNInstance`]
        :param instance_id: 实例id。
        :type instance_id: str
        :param project_id: 项目id。
        :type project_id: str
        :param iam_account: 
        :type iam_account: :class:`huaweicloudsdkddm.v1.IamAccount`
        """
        
        

        self._compressed_databases_info = None
        self._dn_instance = None
        self._instance_id = None
        self._project_id = None
        self._iam_account = None
        self.discriminator = None

        if compressed_databases_info is not None:
            self.compressed_databases_info = compressed_databases_info
        if dn_instance is not None:
            self.dn_instance = dn_instance
        if instance_id is not None:
            self.instance_id = instance_id
        if project_id is not None:
            self.project_id = project_id
        if iam_account is not None:
            self.iam_account = iam_account

    @property
    def compressed_databases_info(self):
        r"""Gets the compressed_databases_info of this LoadSchemaMetadataReq.

        逻辑库信息。

        :return: The compressed_databases_info of this LoadSchemaMetadataReq.
        :rtype: str
        """
        return self._compressed_databases_info

    @compressed_databases_info.setter
    def compressed_databases_info(self, compressed_databases_info):
        r"""Sets the compressed_databases_info of this LoadSchemaMetadataReq.

        逻辑库信息。

        :param compressed_databases_info: The compressed_databases_info of this LoadSchemaMetadataReq.
        :type compressed_databases_info: str
        """
        self._compressed_databases_info = compressed_databases_info

    @property
    def dn_instance(self):
        r"""Gets the dn_instance of this LoadSchemaMetadataReq.

        关联的后端DN信息。

        :return: The dn_instance of this LoadSchemaMetadataReq.
        :rtype: list[:class:`huaweicloudsdkddm.v1.DNInstance`]
        """
        return self._dn_instance

    @dn_instance.setter
    def dn_instance(self, dn_instance):
        r"""Sets the dn_instance of this LoadSchemaMetadataReq.

        关联的后端DN信息。

        :param dn_instance: The dn_instance of this LoadSchemaMetadataReq.
        :type dn_instance: list[:class:`huaweicloudsdkddm.v1.DNInstance`]
        """
        self._dn_instance = dn_instance

    @property
    def instance_id(self):
        r"""Gets the instance_id of this LoadSchemaMetadataReq.

        实例id。

        :return: The instance_id of this LoadSchemaMetadataReq.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this LoadSchemaMetadataReq.

        实例id。

        :param instance_id: The instance_id of this LoadSchemaMetadataReq.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        r"""Gets the project_id of this LoadSchemaMetadataReq.

        项目id。

        :return: The project_id of this LoadSchemaMetadataReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this LoadSchemaMetadataReq.

        项目id。

        :param project_id: The project_id of this LoadSchemaMetadataReq.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def iam_account(self):
        r"""Gets the iam_account of this LoadSchemaMetadataReq.

        :return: The iam_account of this LoadSchemaMetadataReq.
        :rtype: :class:`huaweicloudsdkddm.v1.IamAccount`
        """
        return self._iam_account

    @iam_account.setter
    def iam_account(self, iam_account):
        r"""Sets the iam_account of this LoadSchemaMetadataReq.

        :param iam_account: The iam_account of this LoadSchemaMetadataReq.
        :type iam_account: :class:`huaweicloudsdkddm.v1.IamAccount`
        """
        self._iam_account = iam_account

    def to_dict(self):
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
        if not isinstance(other, LoadSchemaMetadataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
