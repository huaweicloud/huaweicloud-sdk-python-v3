# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchMigrateCloudPhoneRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migrate_infos': 'list[MigrateInfo]'
    }

    attribute_map = {
        'migrate_infos': 'migrate_infos'
    }

    def __init__(self, migrate_infos=None):
        """BatchMigrateCloudPhoneRequestBody

        The model defined in huaweicloud sdk

        :param migrate_infos: 待迁移数据的云手机信息。
        :type migrate_infos: list[:class:`huaweicloudsdkcph.v1.MigrateInfo`]
        """
        
        

        self._migrate_infos = None
        self.discriminator = None

        self.migrate_infos = migrate_infos

    @property
    def migrate_infos(self):
        """Gets the migrate_infos of this BatchMigrateCloudPhoneRequestBody.

        待迁移数据的云手机信息。

        :return: The migrate_infos of this BatchMigrateCloudPhoneRequestBody.
        :rtype: list[:class:`huaweicloudsdkcph.v1.MigrateInfo`]
        """
        return self._migrate_infos

    @migrate_infos.setter
    def migrate_infos(self, migrate_infos):
        """Sets the migrate_infos of this BatchMigrateCloudPhoneRequestBody.

        待迁移数据的云手机信息。

        :param migrate_infos: The migrate_infos of this BatchMigrateCloudPhoneRequestBody.
        :type migrate_infos: list[:class:`huaweicloudsdkcph.v1.MigrateInfo`]
        """
        self._migrate_infos = migrate_infos

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
        if not isinstance(other, BatchMigrateCloudPhoneRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
