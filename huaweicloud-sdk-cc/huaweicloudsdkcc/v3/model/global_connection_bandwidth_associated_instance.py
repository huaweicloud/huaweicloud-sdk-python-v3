# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalConnectionBandwidthAssociatedInstance:

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
        'type': 'str',
        'region_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'region_id': 'region_id',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, type=None, region_id=None, project_id=None):
        r"""GlobalConnectionBandwidthAssociatedInstance

        The model defined in huaweicloud sdk

        :param id: 绑定实例ID。
        :type id: str
        :param type: 绑定实例类型。
        :type type: str
        :param region_id: 绑定实例的region信息，global服务默认取值\&quot;global\&quot;。
        :type region_id: str
        :param project_id: 绑定实例的project id信息。
        :type project_id: str
        """
        
        

        self._id = None
        self._type = None
        self._region_id = None
        self._project_id = None
        self.discriminator = None

        self.id = id
        self.type = type
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def id(self):
        r"""Gets the id of this GlobalConnectionBandwidthAssociatedInstance.

        绑定实例ID。

        :return: The id of this GlobalConnectionBandwidthAssociatedInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GlobalConnectionBandwidthAssociatedInstance.

        绑定实例ID。

        :param id: The id of this GlobalConnectionBandwidthAssociatedInstance.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this GlobalConnectionBandwidthAssociatedInstance.

        绑定实例类型。

        :return: The type of this GlobalConnectionBandwidthAssociatedInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GlobalConnectionBandwidthAssociatedInstance.

        绑定实例类型。

        :param type: The type of this GlobalConnectionBandwidthAssociatedInstance.
        :type type: str
        """
        self._type = type

    @property
    def region_id(self):
        r"""Gets the region_id of this GlobalConnectionBandwidthAssociatedInstance.

        绑定实例的region信息，global服务默认取值\"global\"。

        :return: The region_id of this GlobalConnectionBandwidthAssociatedInstance.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this GlobalConnectionBandwidthAssociatedInstance.

        绑定实例的region信息，global服务默认取值\"global\"。

        :param region_id: The region_id of this GlobalConnectionBandwidthAssociatedInstance.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this GlobalConnectionBandwidthAssociatedInstance.

        绑定实例的project id信息。

        :return: The project_id of this GlobalConnectionBandwidthAssociatedInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this GlobalConnectionBandwidthAssociatedInstance.

        绑定实例的project id信息。

        :param project_id: The project_id of this GlobalConnectionBandwidthAssociatedInstance.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, GlobalConnectionBandwidthAssociatedInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
