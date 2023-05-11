# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QaFlowHitResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'current_node': 'QaFlowHitNodeVo',
        'candidate_nodes': 'list[QaFlowHitNodeVo]',
        'is_completed': 'bool'
    }

    attribute_map = {
        'session_id': 'session_id',
        'current_node': 'current_node',
        'candidate_nodes': 'candidate_nodes',
        'is_completed': 'is_completed'
    }

    def __init__(self, session_id=None, current_node=None, candidate_nodes=None, is_completed=None):
        """QaFlowHitResult

        The model defined in huaweicloud sdk

        :param session_id: seesionID
        :type session_id: str
        :param current_node: 
        :type current_node: :class:`huaweicloudsdkosm.v2.QaFlowHitNodeVo`
        :param candidate_nodes: 备用节点
        :type candidate_nodes: list[:class:`huaweicloudsdkosm.v2.QaFlowHitNodeVo`]
        :param is_completed: 是否完整
        :type is_completed: bool
        """
        
        

        self._session_id = None
        self._current_node = None
        self._candidate_nodes = None
        self._is_completed = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if current_node is not None:
            self.current_node = current_node
        if candidate_nodes is not None:
            self.candidate_nodes = candidate_nodes
        if is_completed is not None:
            self.is_completed = is_completed

    @property
    def session_id(self):
        """Gets the session_id of this QaFlowHitResult.

        seesionID

        :return: The session_id of this QaFlowHitResult.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this QaFlowHitResult.

        seesionID

        :param session_id: The session_id of this QaFlowHitResult.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def current_node(self):
        """Gets the current_node of this QaFlowHitResult.

        :return: The current_node of this QaFlowHitResult.
        :rtype: :class:`huaweicloudsdkosm.v2.QaFlowHitNodeVo`
        """
        return self._current_node

    @current_node.setter
    def current_node(self, current_node):
        """Sets the current_node of this QaFlowHitResult.

        :param current_node: The current_node of this QaFlowHitResult.
        :type current_node: :class:`huaweicloudsdkosm.v2.QaFlowHitNodeVo`
        """
        self._current_node = current_node

    @property
    def candidate_nodes(self):
        """Gets the candidate_nodes of this QaFlowHitResult.

        备用节点

        :return: The candidate_nodes of this QaFlowHitResult.
        :rtype: list[:class:`huaweicloudsdkosm.v2.QaFlowHitNodeVo`]
        """
        return self._candidate_nodes

    @candidate_nodes.setter
    def candidate_nodes(self, candidate_nodes):
        """Sets the candidate_nodes of this QaFlowHitResult.

        备用节点

        :param candidate_nodes: The candidate_nodes of this QaFlowHitResult.
        :type candidate_nodes: list[:class:`huaweicloudsdkosm.v2.QaFlowHitNodeVo`]
        """
        self._candidate_nodes = candidate_nodes

    @property
    def is_completed(self):
        """Gets the is_completed of this QaFlowHitResult.

        是否完整

        :return: The is_completed of this QaFlowHitResult.
        :rtype: bool
        """
        return self._is_completed

    @is_completed.setter
    def is_completed(self, is_completed):
        """Sets the is_completed of this QaFlowHitResult.

        是否完整

        :param is_completed: The is_completed of this QaFlowHitResult.
        :type is_completed: bool
        """
        self._is_completed = is_completed

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
        if not isinstance(other, QaFlowHitResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
