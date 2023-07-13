# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExternalVaultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'protect_type': 'str',
        'region_id': 'str',
        'objcet_type': 'str',
        'cloud_type': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'external_project_id': 'external_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'protect_type': 'protect_type',
        'region_id': 'region_id',
        'objcet_type': 'objcet_type',
        'cloud_type': 'cloud_type',
        'vault_id': 'vault_id'
    }

    def __init__(self, external_project_id=None, limit=None, offset=None, protect_type=None, region_id=None, objcet_type=None, cloud_type=None, vault_id=None):
        """ListExternalVaultRequest

        The model defined in huaweicloud sdk

        :param external_project_id: 其他区域的项目ID
        :type external_project_id: str
        :param limit: 每页显示条目数
        :type limit: int
        :param offset: 偏移值
        :type offset: int
        :param protect_type: [保护类型。取值为backup，replication和hybrid。](tag:hws,hws_hk) [保护类型。取值为backup和replication。](tag:ocb) [保护类型。取值为backup。](tag:g42,hk-g42,sbc,dt,fcs_vm,ctc,tm,tlf,cmcc,hcso_dt)
        :type protect_type: str
        :param region_id: 区域ID
        :type region_id: str
        :param objcet_type: 资源类型
        :type objcet_type: str
        :param cloud_type: [云类型。取值为public和hybrid。](tag:hws,hws_hk) [云类型。取值为public。](tag:g42,hk-g42,sbc,dt,fcs_vm,ctc,ocb,tm,tlf,cmcc,hcso_dt)
        :type cloud_type: str
        :param vault_id: 存储库ID，指定存储ID时其他过滤条件不生效。
        :type vault_id: str
        """
        
        

        self._external_project_id = None
        self._limit = None
        self._offset = None
        self._protect_type = None
        self._region_id = None
        self._objcet_type = None
        self._cloud_type = None
        self._vault_id = None
        self.discriminator = None

        self.external_project_id = external_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if protect_type is not None:
            self.protect_type = protect_type
        self.region_id = region_id
        if objcet_type is not None:
            self.objcet_type = objcet_type
        if cloud_type is not None:
            self.cloud_type = cloud_type
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def external_project_id(self):
        """Gets the external_project_id of this ListExternalVaultRequest.

        其他区域的项目ID

        :return: The external_project_id of this ListExternalVaultRequest.
        :rtype: str
        """
        return self._external_project_id

    @external_project_id.setter
    def external_project_id(self, external_project_id):
        """Sets the external_project_id of this ListExternalVaultRequest.

        其他区域的项目ID

        :param external_project_id: The external_project_id of this ListExternalVaultRequest.
        :type external_project_id: str
        """
        self._external_project_id = external_project_id

    @property
    def limit(self):
        """Gets the limit of this ListExternalVaultRequest.

        每页显示条目数

        :return: The limit of this ListExternalVaultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListExternalVaultRequest.

        每页显示条目数

        :param limit: The limit of this ListExternalVaultRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListExternalVaultRequest.

        偏移值

        :return: The offset of this ListExternalVaultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListExternalVaultRequest.

        偏移值

        :param offset: The offset of this ListExternalVaultRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def protect_type(self):
        """Gets the protect_type of this ListExternalVaultRequest.

        [保护类型。取值为backup，replication和hybrid。](tag:hws,hws_hk) [保护类型。取值为backup和replication。](tag:ocb) [保护类型。取值为backup。](tag:g42,hk-g42,sbc,dt,fcs_vm,ctc,tm,tlf,cmcc,hcso_dt)

        :return: The protect_type of this ListExternalVaultRequest.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        """Sets the protect_type of this ListExternalVaultRequest.

        [保护类型。取值为backup，replication和hybrid。](tag:hws,hws_hk) [保护类型。取值为backup和replication。](tag:ocb) [保护类型。取值为backup。](tag:g42,hk-g42,sbc,dt,fcs_vm,ctc,tm,tlf,cmcc,hcso_dt)

        :param protect_type: The protect_type of this ListExternalVaultRequest.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def region_id(self):
        """Gets the region_id of this ListExternalVaultRequest.

        区域ID

        :return: The region_id of this ListExternalVaultRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListExternalVaultRequest.

        区域ID

        :param region_id: The region_id of this ListExternalVaultRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def objcet_type(self):
        """Gets the objcet_type of this ListExternalVaultRequest.

        资源类型

        :return: The objcet_type of this ListExternalVaultRequest.
        :rtype: str
        """
        return self._objcet_type

    @objcet_type.setter
    def objcet_type(self, objcet_type):
        """Sets the objcet_type of this ListExternalVaultRequest.

        资源类型

        :param objcet_type: The objcet_type of this ListExternalVaultRequest.
        :type objcet_type: str
        """
        self._objcet_type = objcet_type

    @property
    def cloud_type(self):
        """Gets the cloud_type of this ListExternalVaultRequest.

        [云类型。取值为public和hybrid。](tag:hws,hws_hk) [云类型。取值为public。](tag:g42,hk-g42,sbc,dt,fcs_vm,ctc,ocb,tm,tlf,cmcc,hcso_dt)

        :return: The cloud_type of this ListExternalVaultRequest.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this ListExternalVaultRequest.

        [云类型。取值为public和hybrid。](tag:hws,hws_hk) [云类型。取值为public。](tag:g42,hk-g42,sbc,dt,fcs_vm,ctc,ocb,tm,tlf,cmcc,hcso_dt)

        :param cloud_type: The cloud_type of this ListExternalVaultRequest.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def vault_id(self):
        """Gets the vault_id of this ListExternalVaultRequest.

        存储库ID，指定存储ID时其他过滤条件不生效。

        :return: The vault_id of this ListExternalVaultRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this ListExternalVaultRequest.

        存储库ID，指定存储ID时其他过滤条件不生效。

        :param vault_id: The vault_id of this ListExternalVaultRequest.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, ListExternalVaultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
