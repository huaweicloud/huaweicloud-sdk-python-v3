# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentStatusView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_status': 'ComponentStatusType',
        'available_replica': 'int',
        'replica': 'int',
        'fail_detail': 'ComponentFailDetail',
        'last_job_id': 'str',
        'creator': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'artifact': 'ComponentArtifact'
    }

    attribute_map = {
        'component_status': 'component_status',
        'available_replica': 'available_replica',
        'replica': 'replica',
        'fail_detail': 'fail_detail',
        'last_job_id': 'last_job_id',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'artifact': 'artifact'
    }

    def __init__(self, component_status=None, available_replica=None, replica=None, fail_detail=None, last_job_id=None, creator=None, create_time=None, update_time=None, artifact=None):
        r"""ComponentStatusView

        The model defined in huaweicloud sdk

        :param component_status: 
        :type component_status: :class:`huaweicloudsdkservicestage.v3.ComponentStatusType`
        :param available_replica: 
        :type available_replica: int
        :param replica: 
        :type replica: int
        :param fail_detail: 
        :type fail_detail: :class:`huaweicloudsdkservicestage.v3.ComponentFailDetail`
        :param last_job_id: 
        :type last_job_id: str
        :param creator: 
        :type creator: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 修改时间。
        :type update_time: int
        :param artifact: 
        :type artifact: :class:`huaweicloudsdkservicestage.v3.ComponentArtifact`
        """
        
        

        self._component_status = None
        self._available_replica = None
        self._replica = None
        self._fail_detail = None
        self._last_job_id = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self._artifact = None
        self.discriminator = None

        if component_status is not None:
            self.component_status = component_status
        if available_replica is not None:
            self.available_replica = available_replica
        if replica is not None:
            self.replica = replica
        if fail_detail is not None:
            self.fail_detail = fail_detail
        if last_job_id is not None:
            self.last_job_id = last_job_id
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if artifact is not None:
            self.artifact = artifact

    @property
    def component_status(self):
        r"""Gets the component_status of this ComponentStatusView.

        :return: The component_status of this ComponentStatusView.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentStatusType`
        """
        return self._component_status

    @component_status.setter
    def component_status(self, component_status):
        r"""Sets the component_status of this ComponentStatusView.

        :param component_status: The component_status of this ComponentStatusView.
        :type component_status: :class:`huaweicloudsdkservicestage.v3.ComponentStatusType`
        """
        self._component_status = component_status

    @property
    def available_replica(self):
        r"""Gets the available_replica of this ComponentStatusView.

        :return: The available_replica of this ComponentStatusView.
        :rtype: int
        """
        return self._available_replica

    @available_replica.setter
    def available_replica(self, available_replica):
        r"""Sets the available_replica of this ComponentStatusView.

        :param available_replica: The available_replica of this ComponentStatusView.
        :type available_replica: int
        """
        self._available_replica = available_replica

    @property
    def replica(self):
        r"""Gets the replica of this ComponentStatusView.

        :return: The replica of this ComponentStatusView.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        r"""Sets the replica of this ComponentStatusView.

        :param replica: The replica of this ComponentStatusView.
        :type replica: int
        """
        self._replica = replica

    @property
    def fail_detail(self):
        r"""Gets the fail_detail of this ComponentStatusView.

        :return: The fail_detail of this ComponentStatusView.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentFailDetail`
        """
        return self._fail_detail

    @fail_detail.setter
    def fail_detail(self, fail_detail):
        r"""Sets the fail_detail of this ComponentStatusView.

        :param fail_detail: The fail_detail of this ComponentStatusView.
        :type fail_detail: :class:`huaweicloudsdkservicestage.v3.ComponentFailDetail`
        """
        self._fail_detail = fail_detail

    @property
    def last_job_id(self):
        r"""Gets the last_job_id of this ComponentStatusView.

        :return: The last_job_id of this ComponentStatusView.
        :rtype: str
        """
        return self._last_job_id

    @last_job_id.setter
    def last_job_id(self, last_job_id):
        r"""Sets the last_job_id of this ComponentStatusView.

        :param last_job_id: The last_job_id of this ComponentStatusView.
        :type last_job_id: str
        """
        self._last_job_id = last_job_id

    @property
    def creator(self):
        r"""Gets the creator of this ComponentStatusView.

        :return: The creator of this ComponentStatusView.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ComponentStatusView.

        :param creator: The creator of this ComponentStatusView.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this ComponentStatusView.

        创建时间。

        :return: The create_time of this ComponentStatusView.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComponentStatusView.

        创建时间。

        :param create_time: The create_time of this ComponentStatusView.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ComponentStatusView.

        修改时间。

        :return: The update_time of this ComponentStatusView.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ComponentStatusView.

        修改时间。

        :param update_time: The update_time of this ComponentStatusView.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def artifact(self):
        r"""Gets the artifact of this ComponentStatusView.

        :return: The artifact of this ComponentStatusView.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentArtifact`
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        r"""Sets the artifact of this ComponentStatusView.

        :param artifact: The artifact of this ComponentStatusView.
        :type artifact: :class:`huaweicloudsdkservicestage.v3.ComponentArtifact`
        """
        self._artifact = artifact

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
        if not isinstance(other, ComponentStatusView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
