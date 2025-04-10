# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendedProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_space_id': 'str',
        'resource_id': 'str',
        'trial': 'str'
    }

    attribute_map = {
        'work_space_id': 'workSpaceId',
        'resource_id': 'resourceId',
        'trial': 'trial'
    }

    def __init__(self, work_space_id=None, resource_id=None, trial=None):
        r"""ExtendedProperties

        The model defined in huaweicloud sdk

        :param work_space_id: 工作空间ID。
        :type work_space_id: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param trial: 是否是试用集群。
        :type trial: str
        """
        
        

        self._work_space_id = None
        self._resource_id = None
        self._trial = None
        self.discriminator = None

        if work_space_id is not None:
            self.work_space_id = work_space_id
        if resource_id is not None:
            self.resource_id = resource_id
        if trial is not None:
            self.trial = trial

    @property
    def work_space_id(self):
        r"""Gets the work_space_id of this ExtendedProperties.

        工作空间ID。

        :return: The work_space_id of this ExtendedProperties.
        :rtype: str
        """
        return self._work_space_id

    @work_space_id.setter
    def work_space_id(self, work_space_id):
        r"""Sets the work_space_id of this ExtendedProperties.

        工作空间ID。

        :param work_space_id: The work_space_id of this ExtendedProperties.
        :type work_space_id: str
        """
        self._work_space_id = work_space_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ExtendedProperties.

        资源ID。

        :return: The resource_id of this ExtendedProperties.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ExtendedProperties.

        资源ID。

        :param resource_id: The resource_id of this ExtendedProperties.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def trial(self):
        r"""Gets the trial of this ExtendedProperties.

        是否是试用集群。

        :return: The trial of this ExtendedProperties.
        :rtype: str
        """
        return self._trial

    @trial.setter
    def trial(self, trial):
        r"""Sets the trial of this ExtendedProperties.

        是否是试用集群。

        :param trial: The trial of this ExtendedProperties.
        :type trial: str
        """
        self._trial = trial

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
        if not isinstance(other, ExtendedProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
