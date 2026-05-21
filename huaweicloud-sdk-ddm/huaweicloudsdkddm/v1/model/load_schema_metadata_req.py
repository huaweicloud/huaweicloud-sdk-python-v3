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
        'dn_instance': 'list[DNInstance]'
    }

    attribute_map = {
        'compressed_databases_info': 'compressed_databases_info',
        'dn_instance': 'dn_instance'
    }

    def __init__(self, compressed_databases_info=None, dn_instance=None):
        r"""LoadSchemaMetadataReq

        The model defined in huaweicloud sdk

        :param compressed_databases_info: 逻辑库信息。
        :type compressed_databases_info: str
        :param dn_instance: 关联的后端DN信息。
        :type dn_instance: list[:class:`huaweicloudsdkddm.v1.DNInstance`]
        """
        
        

        self._compressed_databases_info = None
        self._dn_instance = None
        self.discriminator = None

        self.compressed_databases_info = compressed_databases_info
        self.dn_instance = dn_instance

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
