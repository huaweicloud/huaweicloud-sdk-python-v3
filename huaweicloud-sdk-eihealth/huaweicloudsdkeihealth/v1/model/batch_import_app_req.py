# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchImportAppReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_project_id': 'str',
        'import_apps': 'list[AppSrcReq]'
    }

    attribute_map = {
        'source_project_id': 'source_project_id',
        'import_apps': 'import_apps'
    }

    def __init__(self, source_project_id=None, import_apps=None):
        """BatchImportAppReq

        The model defined in huaweicloud sdk

        :param source_project_id: 源项目id
        :type source_project_id: str
        :param import_apps: 源应用列表
        :type import_apps: list[:class:`huaweicloudsdkeihealth.v1.AppSrcReq`]
        """
        
        

        self._source_project_id = None
        self._import_apps = None
        self.discriminator = None

        self.source_project_id = source_project_id
        self.import_apps = import_apps

    @property
    def source_project_id(self):
        """Gets the source_project_id of this BatchImportAppReq.

        源项目id

        :return: The source_project_id of this BatchImportAppReq.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this BatchImportAppReq.

        源项目id

        :param source_project_id: The source_project_id of this BatchImportAppReq.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def import_apps(self):
        """Gets the import_apps of this BatchImportAppReq.

        源应用列表

        :return: The import_apps of this BatchImportAppReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppSrcReq`]
        """
        return self._import_apps

    @import_apps.setter
    def import_apps(self, import_apps):
        """Sets the import_apps of this BatchImportAppReq.

        源应用列表

        :param import_apps: The import_apps of this BatchImportAppReq.
        :type import_apps: list[:class:`huaweicloudsdkeihealth.v1.AppSrcReq`]
        """
        self._import_apps = import_apps

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
        if not isinstance(other, BatchImportAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
