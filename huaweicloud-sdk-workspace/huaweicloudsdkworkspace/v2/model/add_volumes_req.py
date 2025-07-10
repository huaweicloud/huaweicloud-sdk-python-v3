# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddVolumesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'volumes': 'list[Volume]'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'volumes': 'volumes'
    }

    def __init__(self, enterprise_project_id=None, volumes=None):
        r"""AddVolumesReq

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param volumes: 待新增的磁盘信息，每个桌面的数据盘数量不超过10个。
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        
        

        self._enterprise_project_id = None
        self._volumes = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.volumes = volumes

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AddVolumesReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this AddVolumesReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AddVolumesReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this AddVolumesReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def volumes(self):
        r"""Gets the volumes of this AddVolumesReq.

        待新增的磁盘信息，每个桌面的数据盘数量不超过10个。

        :return: The volumes of this AddVolumesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this AddVolumesReq.

        待新增的磁盘信息，每个桌面的数据盘数量不超过10个。

        :param volumes: The volumes of this AddVolumesReq.
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        self._volumes = volumes

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
        if not isinstance(other, AddVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
